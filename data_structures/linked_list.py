from typing import TypeVar, Generic

T = TypeVar('T')

class LinkedListNode(Generic[T]):
  def __init__(self, data: T):
    self.data = data
    self.next = None

class LinkedList(Generic[T]):
  def __init__(self, data: T = None):
    if data:
      new_node = LinkedListNode[T](data)
      self.head = new_node
      self.tail = new_node
      self.length = 1
    else:
      self.head = None
      self.tail = None
      self.length = 0

  def append(self, data: T):
    new_node = LinkedListNode[T](data)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
      self.length = 1
    else:
      self.tail.next = new_node
      self.tail = new_node
      self.length += 1
    return new_node
  
  def print(self) -> None:
    cur_node = self.head
    while (cur_node.next):
      print(cur_node.data)
      cur_node = cur_node.next
    print(cur_node.data)

  def prepend(self, data: T) -> LinkedListNode[T]:
    if self.length == 0:
      new_node = self.append(data)
      return new_node
    else:
      new_node = LinkedListNode[T](data)
      new_node.next = self.head
      self.head = new_node
      self.length += 1
      return new_node

  def pop(self) -> LinkedListNode[T]:
    if self.length == 0:
      return None
    elif self.length == 1:
      cur_node = self.head
      self.head = None
      self.tail = None
      self.length = 0
      return cur_node
    
    cur_node = self.head
    prev_node = self.head
    while(cur_node.next):
      prev_node = cur_node
      cur_node = cur_node.next
    
    self.tail = prev_node
    self.tail.next = None
    self.length -= 1
    return cur_node

  def pop_first(self) -> LinkedListNode[T]:
    if self.length == 0:
      return None
    else:
      cur_node = self.head
      self.head = self.head.next
      self.length -= 1
      return cur_node

  def set_data(self, position: int, data: T) -> LinkedListNode[T]:
    if self.length == 0:
      return None
    else:
      cur_node = self.head
      index = 0
      while index < position:
        cur_node = cur_node.next
        index += 1
      cur_node.data = data
      return cur_node

  def get_data(self, position: int) -> LinkedListNode[T]:
    if self.length == 0:
      return None
    else:
      cur_node = self.head
      index = 0
      while index < position:
        cur_node = cur_node.next
        index += 1
      return cur_node

  def insert(self, position: int, data: T) -> LinkedListNode[T]:
    if position > self.length:
      return None
    elif self.length == 0:
      return self.append(data)
    elif position == 0:
      return self.prepend(data)
    else:
      new_node = LinkedListNode[T](data)
      index = 0
      cur_node = self.head
      prev_node = self.head
      while index <= position:
        prev_node = cur_node
        cur_node = cur_node.next
        index += 1

      prev_node.next = new_node
      new_node.next = cur_node
      self.length += 1
      return new_node
  
  def remove(self, position: int) -> LinkedListNode[T]:
    if self.length == 0 or position > self.length:
      return None
    elif position == 0:
      cur_node = self.head
      self.head = self.head.next
      self.length -= 1
      return cur_node
    else:
      cur_node = self.head
      prev_node = self.head
      index = 0
      while index < position:
        prev_node = cur_node
        cur_node = cur_node.next
        index += 1

      if position == self.length:
        prev_node.next = None
      else:
        prev_node.next = cur_node.next

      return cur_node

  # TODO:
  def reverse(self) -> None:
    pass

def tester():
  num_linked_list = LinkedList[int]()

  for num in range(1, 11):
    num_linked_list.append(num * 10)
  print(f'Length of the linked list is {num_linked_list.length}')

  for num in range(0, 4):
    num_linked_list.prepend(-num * 10)

  num_linked_list.insert(7, 3.5)
  num_linked_list.insert(0, -40)
  num_linked_list.print()

  print(f'Value at position 7 is: {num_linked_list.get_data(7).data}')
  print(f'New Value at position 7 is: {num_linked_list.set_data(7, 3.3876).data}')

  print(f'Length before pop: {num_linked_list.length} Popped value: {num_linked_list.pop().data} Length after pop: {num_linked_list.length}');

  print(f'Length before pop: {num_linked_list.length} Popped value: {num_linked_list.pop().data} Length after pop: {num_linked_list.length}');

  str_linked_list = LinkedList[str]('Puma')
  for item in ['Nike', 'Hoka', 'On', 'Brooks', 'Skechers']:
    print(f'New node appended: {str_linked_list.append(item).data}')

  for item in ['Adidas', 'New Balance']:
    print(f'New node prepended: {str_linked_list.prepend(item).data}')

  str_linked_list.print()

  print(f'Item removed ad 3: {str_linked_list.remove(3).data}')

  str_linked_list.print()

if __name__ == '__main__':
  tester()