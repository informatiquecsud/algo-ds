from typing import TypeVar, Generic

T = TypeVar("T")


class Container(Generic[T]):

    def __init__(self, items: list[T]):
        self._items: list[T] = items

    def get_items(self) -> list[T]:
        return self._items


# c1 contient ne contient que des entiers
c1 = Container([1, 2, 3, 4])
print(c1.get_items())

c2 = Container(["Nina", "Jonathan"])
print(c2.get_items())
