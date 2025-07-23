"""Core dispatch mechanism."""

import asyncio
import inspect
from collections.abc import Sequence
from typing import (
    Any,
    Protocol,
    TypeAlias,
    TypeGuard,
    Union,
)


Message: TypeAlias = Union[object, Sequence[object]]


class Responsive(Protocol):
    """Protocol for objects with ``react`` field."""

    react: Any


def is_responsive(obj: object) -> TypeGuard[Responsive]:
    """Check whether ``obj`` has a ``reactaa member."""
    return hasattr(obj, "react")


class Dispatcher:
    """Message dispatcher.

    The dispatcher carries out the following steps:

    - Receive and enqueue messages.
    - Dequeue one message.
    - Determine ``react`` method.
    - Collect messages from running ``react`` method.
    - Repeat or exit.

    :param maxsize: passed to queue
    """

    def __init__(self, /, maxsize: int = 0) -> None:
        """Initialize the dispatcher."""
        self._message_queue: asyncio.Queue[Message] = asyncio.Queue(maxsize=maxsize)
        self._loop_task: asyncio.Task | None = None

    async def dispatch(self, message: Message) -> None:
        """Dispatch a single message.

        :param message: the message for dispatch.
        """
        match message:
            case [receiver, *args]:
                await self._dispatch(receiver, args)
            case _:
                await self._dispatch(message, ())

    async def _dispatch(
        self,
        receiver: object,
        args: Sequence[object],
    ) -> None:
        """Dispatch a single message.

        :param receiver: the receiver of the message
        :param args: the message arguments.
        """
        if not is_responsive(receiver):
            await self.dispose(receiver, args)
            return
        react = receiver.react

        if inspect.iscoroutinefunction(react):
            result = await receiver.react(*args)
            await self.receive(result)

        elif inspect.isasyncgenfunction(react):
            async for message in receiver.react(*args):
                await self.receive(message)

        else:
            result = receiver.react(*args)
            if inspect.isgenerator(result):
                for message in result:
                    await self.receive(message)
            else:
                await self.receive(result)

    async def receive(self, message: Message) -> None:
        """Receive and enqueue a single message.

        :param message: the received message.
        """
        await self._message_queue.put(message)

    async def dispose(
        self,
        receiver: object,
        args: Sequence[object],
    ) -> None:
        """Dispose a message without ``react`` method.

        Feel free to override this method in order
        to change behavior.

        :param receiver: the receiver of the message
        :param args: the message arguments.
        """
        pass

    def start(self) -> bool:
        """Start the dispatcher loop as a new task.

        If this dispatcher has already a loop running
        this method does nothing.

        :return: whether a new loop was started
        """
        if self._loop_task is not None:
            return False
        coro = self._loop()
        self._loop_task = asyncio.create_task(coro)
        return True

    async def _loop(self) -> None:
        """Run the dispatcher loop."""
        async with asyncio.TaskGroup() as tg:
            while True:
                message = await self._message_queue.get()
                tg.create_task(self.dispatch(message))
