import unittest

from stack import Stack


class TestStack(unittest.TestCase):
  def test_new_stack_is_empty(self):
    s = Stack()
    self.assertTrue(s.is_empty())
    self.assertEqual(s.size(), 0)
    self.assertEqual(len(s), 0)
    self.assertEqual(s.to_list(), [])

  def test_pop_empty(self):
    self.assertIsNone(Stack().pop())

  def test_peek_empty(self):
    self.assertIsNone(Stack().peek())

  def test_clear_empty(self):
    s = Stack()
    s.clear()
    self.assertTrue(s.is_empty())
    self.assertEqual(s.size(), 0)

  def test_push_updates_state(self):
    s = Stack()
    s.push(1)
    self.assertFalse(s.is_empty())
    self.assertEqual(s.size(), 1)
    self.assertEqual(len(s), 1)
    s.push(2)
    self.assertEqual(s.size(), 2)
    self.assertEqual(len(s), 2)

  def test_lifo_order(self):
    s = Stack()
    for i in (1, 2, 3):
      s.push(i)
    self.assertEqual([s.pop(), s.pop(), s.pop()], [3, 2, 1])

  def test_pop_to_empty(self):
    s = Stack()
    s.push(1)
    self.assertEqual(s.pop(), 1)
    self.assertTrue(s.is_empty())
    self.assertEqual(s.size(), 0)
    self.assertEqual(len(s), 0)
    self.assertIsNone(s.pop())

  def test_peek_does_not_remove(self):
    s = Stack()
    s.push(1)
    s.push(2)
    self.assertEqual(s.peek(), 2)
    self.assertEqual(s.peek(), 2)
    self.assertEqual(s.size(), 2)

  def test_clear(self):
    s = Stack()
    s.push(1)
    s.push(2)
    s.clear()
    self.assertTrue(s.is_empty())
    self.assertEqual(s.size(), 0)
    self.assertEqual(len(s), 0)
    self.assertIsNone(s.pop())
    self.assertIsNone(s.peek())

  def test_reuse_after_clear(self):
    s = Stack()
    s.push(1)
    s.clear()
    s.push(5)
    self.assertEqual(s.peek(), 5)
    self.assertEqual(s.to_list(), [5])

  def test_to_list_bottom_first(self):
    s = Stack()
    for i in (1, 2, 3):
      s.push(i)
    self.assertEqual(s.to_list(), [1, 2, 3])

  def test_to_list_is_copy(self):
    s = Stack()
    s.push(1)
    s.push(2)
    out = s.to_list()
    out.append(99)
    out[0] = 42
    self.assertEqual(s.to_list(), [1, 2])
    self.assertEqual(s.size(), 2)

  def test_falsy_values(self):
    s = Stack()
    for v in (0, '', False):
      s.push(v)
    self.assertEqual(s.size(), 3)
    self.assertFalse(s.is_empty())
    self.assertIs(s.peek(), False)
    self.assertIs(s.pop(), False)
    self.assertEqual(s.pop(), '')
    self.assertEqual(s.pop(), 0)
    self.assertTrue(s.is_empty())

  def test_push_none(self):
    s = Stack()
    s.push(None)
    self.assertFalse(s.is_empty())
    self.assertEqual(s.size(), 1)
    self.assertIsNone(s.peek())
    self.assertEqual(s.to_list(), [None])
    self.assertIsNone(s.pop())
    self.assertTrue(s.is_empty())


if __name__ == '__main__':
  unittest.main()
