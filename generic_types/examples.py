
class Container[T]:

    def __init__(self, items: list[T]):
        self._items: list[T] = items

    def get_items(self) -> list[T]:
        return self._items

