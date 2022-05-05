"""LeetCode Problem 225 - Implement Stack Using Queues

Implement a last-in-first-out (LIFO) stack using only two queues. The
implemented stack should support all the functions of a normal stack (push, top,
pop, and empty).

Implement the MyStack class:

    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes
=====
 * You must use only standard operations of a queue, which means that only push
   to back, peek/pop from front, size and is empty operations are valid.
 * Depending on your language, the queue may not be supported natively. You may
   simulate a queue using a list or deque (double-ended queue) as long as you
   use only a queue's standard operations.


Constraints
===========
 * 1 <= x <= 9
 * At most 100 calls will be made to push, pop, top, and empty.
 * All the calls to pop and top are valid.

"""

from collections import deque
from typing import Generic, Optional, T


class Stack(Generic[T]):
    """Stack Implementation"""

    def __init__(self) -> None:
        """Stack Constructor"""
        self._a = deque()
        self._b = deque()

    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self._a.append(item)

    def pop(self) -> Optional[T]:
        """Pop the top element on the stack, if there is one."""
        if self.empty():
            return None

        while len(self._a) > 1:
            self._b.append(self._a.popleft())

        top_element = self._a.popleft()

        while len(self._b):
            self._a.append(self._b.popleft())

        return top_element

    def top(self) -> Optional[T]:
        """View the next element in the stack without popping it."""
        if self.empty():
            return None

        while len(self._a) > 1:
            self._b.append(self._a.popleft())

        top_element = self._a.popleft()

        while len(self._b):
            self._a.append(self._b.popleft())

        self._a.append(top_element)

        return top_element

    def empty(self) -> bool:
        """Return true if there are no items in the queue, or false otherwise."""
        return len(self._a) == 0
