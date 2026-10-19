from typing import TypeVar, Generic

T = TypeVar('T')

class DoublyLinkedListNode(Generic[T]):
  def __init__(self, data: T):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList(Generic[T]):
  def __init__(self, data: T = None):
    if data is not None:
      new_node = DoublyLinkedListNode[T](data)
      self.head = new_node
      self.tail = new_node
      self.length = 1
    else:
      self.head = None
      self.tail = None
      self.length = 0

  def __len__(self) -> int:
    return self.length

  def push(self, data: T) -> DoublyLinkedListNode[T]:
    new_node = DoublyLinkedListNode[T](data)
    if self.length == 0:
      self.head = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
    self.tail = new_node
    self.length += 1
    return new_node

  def pop(self) -> DoublyLinkedListNode[T] | None:
    if self.length == 0:
      return None
    cur_node = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = cur_node.prev
      self.tail.next = None
      cur_node.prev = None
    self.length -= 1
    return cur_node

  def _get_node(self, position: int) -> DoublyLinkedListNode[T]:
    if position < self.length // 2:
      cur_node = self.head
      for _ in range(position):
        cur_node = cur_node.next
    else:
      cur_node = self.tail
      for _ in range(self.length - 1 - position):
        cur_node = cur_node.prev
    return cur_node

  def insert(self, position: int, data: T) -> DoublyLinkedListNode[T] | None:
    if position < 0 or position > self.length:
      return None
    if position == self.length:
      return self.push(data)
    new_node = DoublyLinkedListNode[T](data)
    next_node = self._get_node(position)
    prev_node = next_node.prev
    new_node.next = next_node
    new_node.prev = prev_node
    next_node.prev = new_node
    if prev_node is None:
      self.head = new_node
    else:
      prev_node.next = new_node
    self.length += 1
    return new_node

  def remove(self, position: int) -> DoublyLinkedListNode[T] | None:
    if position < 0 or position >= self.length:
      return None
    cur_node = self._get_node(position)
    prev_node = cur_node.prev
    next_node = cur_node.next
    if prev_node is None:
      self.head = next_node
    else:
      prev_node.next = next_node
    if next_node is None:
      self.tail = prev_node
    else:
      next_node.prev = prev_node
    cur_node.next = None
    cur_node.prev = None
    self.length -= 1
    return cur_node

  def print(self) -> None:
    cur_node = self.head
    while cur_node is not None:
      print(cur_node.data)
      cur_node = cur_node.next
