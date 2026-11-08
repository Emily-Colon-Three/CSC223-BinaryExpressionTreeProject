"""The Stack class acts as a basic Stack adapter of the existing Python list. Using a list,
it creates an interface to stack items on top of one another and easily handle data in the
stack structure. This is superior to a simple list for the same use because it leaves out
unnecessary options such as accessing item by index or searching the stack.
Upon initialization, an empty stack is created. An item is added to the top of the stack
with push(item), or taken from the top of the stack with pop(), which only functions if
there is an item to remove, raising IndexError if not. peek() functions similarly, but
only returns the top item rather than popping it off.
Then, is_empty() simply returns a boolean, True if the stack is empty, False if size is
above 0. size() simply returns self._size."""
class Stack:
    def __init__(self):
        self._items = []
        self._size = 0

    def push(self, item):
        self._items.append(item)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')

        self._size -= 1 # When popping an item off stack, size must be adjusted.
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')

        return self._items[-1]

    def is_empty(self) -> bool:
        if self._size == 0:
            return True
        else:
            return False

    def size(self) -> int:
        return self._size

import unittest

# Tests that a newly created stack is empty. Also that is_empty() works as intended.
class InitializeStack(unittest.TestCase):
    def test_empty(self):
        stack = Stack()
        self.assertEqual(stack.is_empty(), True)
        self.assertEqual(stack.size(), 0)

# Tests that push(item) causes correct changes. Tests push, pop, and peek.
class UpdateStack(unittest.TestCase):
    def setUp(self): # Creates stack and pushes a 1, then a 2. 2 is now top item.
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(2)

    def test_size(self): # Tests that the size has been updated accordingly from empty.
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 2)

    def test_pop_and_peek(self): # Tests that peek() only returns top, and that pop() successfully removes and returns it.
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.pop(), 2) # 2 removed from stack, only 1 remains.

        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(self.stack.size(), 1)