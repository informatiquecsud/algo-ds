
from stack import StackADT
from typing import TypeVar, Generic

T = TypeVar('T')

class ListStack(StackADT[T], Generic[T]):
    '''

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
    >>> s
    []

    '''

    def __init__(self) -> None:
        self._items = []

    def __repr__(self) -> str:
        return repr(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        try:
            return self._items.pop()
        except IndexError as e:
            raise EmptyStackError('Pop from an empty stack') from e

    def peek(self) -> T:
        try:
            return self._items[-1]
        except IndexError as e:
            raise EmptyStackError('Peek an empty stack') from e

    def is_empty(self) -> bool:
        return len(self) == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()