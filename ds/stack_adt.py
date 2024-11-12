from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class StackADT(ABC, Generic[T]):

    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def peek(self) -> T:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
