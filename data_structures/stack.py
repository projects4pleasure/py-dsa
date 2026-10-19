from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
  def __init__(self):
    self._items: list[T] = []

  def __len__(self) -> int:
    return len(self._items)

  def push(self, data: T) -> None:
    self._items.append(data)

  def pop(self) -> T | None:
    if not self._items:
      return None
    return self._items.pop()

  def peek(self) -> T | None:
    if not self._items:
      return None
    return self._items[-1]

  def is_empty(self) -> bool:
    return len(self._items) == 0

  def size(self) -> int:
    return len(self._items)

  def clear(self) -> None:
    self._items.clear()

  def to_list(self) -> list[T]:
    return list(self._items)
