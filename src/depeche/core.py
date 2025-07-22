"""Core dispatch mechanism."""

import asyncio
import inspect
from collections.abc import Sequence
from typing import TypeAlias, Union


Message: TypeAlias = Union[object, Sequence[object]]


class Dispatcher:
    """Message dispatcher.

    The dispatcher carries out the following steps:

    - Receive and enqueue messages.
    - Dequeue one message.
    - Determine ``react`` method.
    - Collect messages from running ``react`` method.
    - Repeat or exit.
    """

    def __init__(self) -> None:
        """Initialize the dispatcher."""
        self._message_queue: asyncio.Queue[Message] = asyncio.Queue()

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
        if not hasattr(receiver, "react"):
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
