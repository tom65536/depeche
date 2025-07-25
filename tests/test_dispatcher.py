"""Test cases for the dispatcher."""

from collections.abc import Sequence

from rsvp.core import Dispatcher

import pytest


class XDispatcher(Dispatcher):
   """Counts dispose calls."""

   def __init__(self) -> None:
      """Initialize."""
      super().__init__()
      self.count: int = 0

   async def dispose(
      self,
      receiver: object,
      args: Sequence[object],
   ) -> None:
      """Dispose message without ``react``."""
      self.count += 1


class FooReg:
   """Class with regular react method."""

   count: int = 0

   def react(self, arg: int):
      """React."""
      self.count += arg
      return self.__class__.__name__


class FooGen:
   """Class with generator react method."""

   count: int = 0

   def react(self):
      """React."""
      self.count += 1
      yield self.__class__.__name__
      yield self.__class__.__name__
      self.count += 1


class FooCoro:
   """Class with coroutine react method."""

   count: int = 0

   async def react(self):
      """React."""
      self.count += 1
      return self.__class__.__name__


class FooAGen:
   """Class with async generator react method."""

   count: int = 0

   async def react(self):
      """React."""
      self.count += 1
      yield self.__class__.__name__
      yield self.__class__.__name__
      self.count += 1


@pytest.mark.asyncio
async def test_dispatch_dispose() -> None:
   """Test the dispatch method without a function."""
   dis = XDispatcher()
   msg = 'no message'

   await dis.dispatch(msg)

   assert dis.count == 1


@pytest.mark.asyncio
async def test_dispatch_function() -> None:
   """Test the dispatch method with a function."""
   dis = XDispatcher()
   receiver = FooReg()
   msg = (receiver, 7)

   await dis.dispatch(msg)

   assert receiver.count == 7
   assert dis.count == 0


@pytest.mark.asyncio
async def test_dispatch_generator() -> None:
   """Test the dispatch method with a generator."""
   dis = XDispatcher()
   msg = FooGen()

   await dis.dispatch(msg)

   assert msg.count == 2
   assert dis.count == 0


@pytest.mark.asyncio
async def test_dispatch_coro() -> None:
   """Test the dispatch method with a coroutine."""
   dis = XDispatcher()
   msg = FooCoro()

   await dis.dispatch(msg)

   assert msg.count == 1
   assert dis.count == 0


@pytest.mark.asyncio
async def test_dispatch_agen() -> None:
   """Test the dispatch method with a coroutine."""
   dis = XDispatcher()
   msg = FooAGen()

   await dis.dispatch(msg)

   assert msg.count == 2
   assert dis.count == 0
