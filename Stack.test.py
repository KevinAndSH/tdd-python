import unittest
import math
import random

class StackNode():
    def __init__(self, value):
        self.value = value
        self._next = None

    def get_next(self):
        return self._next

    def set_next(self, next):
        self._next = next

    next = property(get_next, set_next)


class Stack():
    def __init__(self, max_size = math.inf):
        self._size = 0
        self._max_size = max_size
        self._head = StackNode(None)

    def get_size(self):
        return self._size

    size = property(get_size)

    def push(self, value):
        if self.size == self._max_size:
            raise Exception("Stack Overflow")

        new_node = StackNode(value)
        new_node.next = self._head.next
        self._head.next = new_node

        self._size += 1

    def pop(self):
        if self.is_empty():
            return

        removed_value = self.peek()
        self._head.next = self._head.next.next
        self._size -= 1
        return removed_value

    def peek(self):
        return self._head.next.value

    def is_empty(self):
        return self._size == 0


class Stack_tests(unittest.TestCase):
    def test_size(self):
        my_stack = Stack()
        # given: stack is empty
        # when: nothing is pushed
        # then: size is 0
        self.assertEqual(my_stack.size, 0)

        my_stack.push(1)
        # given: size is 0
        # when: something is pushed
        # then: size is 1
        self.assertEqual(my_stack.size, 1)

        my_stack.push(1)
        # given: size is 1
        # when: something is pushed
        # then: size is 2
        self.assertEqual(my_stack.size, 2)

        my_stack.pop()
        my_stack.pop()
        # given: size is 2
        # when: something is removed from the stack twice
        # then: size is 0
        self.assertEqual(my_stack.size, 0)

        my_stack.pop()
        # given: size is 0
        # when: pop() method is called
        # then: size is still 0
        self.assertEqual(my_stack.size, 0)

    def test_push_and_peek(self):
        my_stack = Stack()

        ran1 = random.random()
        my_stack.push(ran1)
        # given: stack
        # when: something is pushed
        # then: peek() returns that something
        self.assertEqual(my_stack.peek(), ran1)

        ran2 = random.random()
        my_stack.push(ran2)
        # given: stack
        # when: something is pushed
        # then: peek() returns that something
        self.assertEqual(my_stack.peek(), ran2)

    def test_push_and_pop(self):
        my_stack = Stack()

        ran1 = random.random()
        my_stack.push(ran1)
        # given: stack
        # when: something is pushed
        # then: pop() returns that something
        self.assertEqual(my_stack.pop(), ran1)

        ran2 = random.random()
        my_stack.push(ran2)
        # given: stack
        # when: something is pushed
        # then: pop() returns that something
        self.assertEqual(my_stack.pop(), ran2)

    def test_is_empty(self):
        my_stack = Stack()

        # given: stack was just created
        # when: nothing is pushed yet
        # then: is_empty() returns true
        self.assertTrue(my_stack.is_empty())

        my_stack.push(1)
        # given: stack is empty
        # when: something is pushed
        # then: is_empty() returns false
        self.assertFalse(my_stack.is_empty())

        my_stack.pop()
        # given: stack has 1 element
        # when: something is removed from the stack
        # then: is_empty() returns true
        self.assertTrue(my_stack.is_empty())

    def test_stack_overflow(self):
        my_stack = Stack(2)

        my_stack.push(1)
        my_stack.push(1)

        # given: stack is full
        # when: something is pushed above the maximum capacity
        # then: stack overflow exception is raised
        with self.assertRaises(Exception):
            my_stack.push(1)

        # given: stack is full
        # when: something is pushed above the maximum capacity
        # then: stack size is unchanged
        self.assertEqual(my_stack.size, 2)


if __name__ == "__main__":
    unittest.main()

