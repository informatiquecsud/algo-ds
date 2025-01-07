from typing import TypeVar, Generic
from .stack import StackADT

T = TypeVar("T")

class ListStack(StackADT[T], Generic[T]):
    """

    ``ListStack`` implements a stack by using a list as the container.

    >>> s: ListStack[int] = ListStack()
    >>> s.push(1)
    >>> s
    [1]
    >>> s.push(2)
    >>> s
    [1, 2]
    >>> s.push(3)
    >>> s
    [1, 2, 3]
    >>> s.peek()
    3
    >>> s.pop()
    3
    >>> s
    [1, 2]
    >>> s.pop()
    2
    >>> s.pop()
    1
    >>> s.pop()
    Traceback (most recent call last):
    ...
    EmptyStackError: Pop from an empty stack
    >>> s.peek()
    Traceback (most recent call last):
    ...
    EmptyStackError: Peek an empty stack
    >>> s
    []

    """

    def __init__(self) -> None:
        self._items: list[T] = []

    def __repr__(self) -> str:
        return repr(self._items)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
