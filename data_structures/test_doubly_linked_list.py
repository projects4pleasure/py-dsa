import io
import unittest
from contextlib import redirect_stdout

from doubly_linked_list import DoublyLinkedList


def forward(lst):
  out = []
  cur_node = lst.head
  while cur_node is not None:
    out.append(cur_node.data)
    cur_node = cur_node.next
  return out


def backward(lst):
  out = []
  cur_node = lst.tail
  while cur_node is not None:
    out.append(cur_node.data)
    cur_node = cur_node.prev
  return out


def make(*values):
  lst = DoublyLinkedList()
  for v in values:
    lst.push(v)
  return lst


class DoublyLinkedListTest(unittest.TestCase):
  def check(self, lst, expected):
    self.assertEqual(forward(lst), expected)
    self.assertEqual(backward(lst), expected[::-1])
    self.assertEqual(lst.length, len(expected))
    self.assertEqual(len(lst), len(expected))
    if expected:
      self.assertIsNone(lst.head.prev)
      self.assertIsNone(lst.tail.next)
    else:
      self.assertIsNone(lst.head)
      self.assertIsNone(lst.tail)

  def test_init(self):
    self.check(DoublyLinkedList(), [])
    self.check(DoublyLinkedList(5), [5])
    self.check(DoublyLinkedList(0), [0])
    self.check(DoublyLinkedList(''), [''])

  def test_push(self):
    lst = DoublyLinkedList()
    node = lst.push(1)
    self.assertIs(lst.head, node)
    self.assertIs(lst.tail, node)
    lst.push(0)
    lst.push(3)
    self.check(lst, [1, 0, 3])

  def test_pop(self):
    lst = DoublyLinkedList()
    self.assertIsNone(lst.pop())
    lst = make(1, 2, 3)
    node = lst.pop()
    self.assertEqual(node.data, 3)
    self.assertIsNone(node.prev)
    self.check(lst, [1, 2])
    lst.pop()
    self.assertEqual(lst.pop().data, 1)
    self.check(lst, [])
    self.assertIsNone(lst.pop())

  def test_insert(self):
    lst = make(1, 2)
    node = lst.insert(0, 0)
    self.assertIs(lst.head, node)
    self.check(lst, [0, 1, 2])
    node = lst.insert(3, 9)
    self.assertIs(lst.tail, node)
    self.check(lst, [0, 1, 2, 9])
    node = lst.insert(2, 5)
    self.assertIs(node.prev.next, node)
    self.assertIs(node.next.prev, node)
    self.check(lst, [0, 1, 5, 2, 9])

  def test_insert_empty_and_falsy(self):
    lst = DoublyLinkedList()
    self.assertIsNotNone(lst.insert(0, 0))
    self.check(lst, [0])

  def test_insert_out_of_range(self):
    lst = make(1, 2)
    self.assertIsNone(lst.insert(-1, 7))
    self.assertIsNone(lst.insert(3, 7))
    self.check(lst, [1, 2])

  def test_remove(self):
    lst = make(1, 2, 3, 4, 5)
    self.assertEqual(lst.remove(0).data, 1)
    self.check(lst, [2, 3, 4, 5])
    self.assertEqual(lst.remove(3).data, 5)
    self.check(lst, [2, 3, 4])
    node = lst.remove(1)
    self.assertEqual(node.data, 3)
    self.assertIsNone(node.next)
    self.assertIsNone(node.prev)
    self.check(lst, [2, 4])

  def test_remove_single_and_empty(self):
    lst = make(0)
    self.assertEqual(lst.remove(0).data, 0)
    self.check(lst, [])
    self.assertIsNone(lst.remove(0))

  def test_remove_out_of_range(self):
    lst = make(1, 2)
    self.assertIsNone(lst.remove(-1))
    self.assertIsNone(lst.remove(2))
    self.check(lst, [1, 2])

  def test_print(self):
    buf = io.StringIO()
    with redirect_stdout(buf):
      DoublyLinkedList().print()
    self.assertEqual(buf.getvalue(), '')
    buf = io.StringIO()
    with redirect_stdout(buf):
      make(1, 0, 3).print()
    self.assertEqual(buf.getvalue(), '1\n0\n3\n')


if __name__ == '__main__':
  unittest.main()
