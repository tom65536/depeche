"""Type definitions."""

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
   """Check whether ``obj`` has a ``react`` member.

   :param obj: the examined object
   :return: true if the ``obj`` is ``Responsive``
   """
   return hasattr(obj, 'react')
