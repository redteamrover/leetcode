"""LeetCode Problem 844 - Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints
===========
 * 1 <= s.length, t.length <= 200
 * s and t only contain lowercase letters and '#' characters.

"""

import unittest

from typing import Generic, Optional, T, Text
from unittest import TestCase


class Stack(Generic[T]):
    """Generic Stack Container Class"""

    def __init__(self) -> None:
        """Stack Constructor"""
        # Initialize the stack's items to an empty list.
        self._items = []

        # Initialize the stack size to zero elements.
        self._size = 0

    def __eq__(self, other: "Stack") -> bool:
        """Return true if the stacks have the same elements in the same order."""
        # The first check that needs to occur is whether the two stacks have the
        # same number of elements.
        if len(self) != len(other):
            # If they do not, then they obviously differ in their content, and
            # are therefore not equal to one another.
            return False

        # If both stacks have the same number of elements, check that each of
        # their respective elements matches that in the other stack.
        for a, b in zip(self._items, other._items):
            # Check whether the two elements match.
            if a != b:
                # If they do not, we know the stacks are not equal to one
                # another, and we can therefore simply return immediately.
                return False

        # If no differences are found between the stack elements, then the
        # stacks are equal to each other.
        return True

    def __len__(self) -> int:
        """Return the size of the stack."""
        return self._size

    def __repr__(self) -> Text:
        """Return descriptive text representation of the stack."""
        return f"Stack({self})"

    def __str__(self) -> Text:
        """Return text representation of the stack items."""
        return "[" + ", ".join(str(item) for item in self._items) + "]"

    def peek(self) -> Optional[T]:
        """Peek

        View the top-most item on the stack without popping it, if there is one.
        """
        return self._items[-1] if self._items else None

    def push(self, item: T) -> None:
        """Add an item onto the stack."""
        # Add the item to the stack.
        self._items.append(item)

        # Increment the size of the stack.
        self._size += 1

    def pop(self) -> Optional[T]:
        """Remove and return the top-most item on the stack, if there is one."""
        # If there are no items to pop, just return nothing without doing
        # anything.
        if not self._items:
            return None

        # Since we actually have to pop an item from the stack, decrement the
        # size of the stack prior to returning the popped item.
        self._size -= 1

        # Go ahead and pop the top-most item from the stack, and return the item
        # to the caller.
        return self._items.pop()


def create_stack_representation(string: Text) -> Stack[Text]:
    """Create a Stack Representing the Final String State"""
    # Initialize the stack.
    stack = Stack()

    # Iterate over each character in the input string.
    for character in string:
        # First, check whether the current input character represents a deletion
        # via a backspace character press.
        if character == "#":
            # Delete the previous character in the string by popping it off of
            # the stack.
            stack.pop()

            # Move on to the next character.
            continue

        # Otherwise, simply add the current character to the stack.
        stack.push(character)

    # Finally, return the populated stack.
    return stack


def backspace_compare(s: Text, t: Text) -> bool:
    """Backspace Compare

    Given two strings, s and t, return True if they are equal when both are
    typed into empty text editors, with the pound character representing a
    backspace character.
    """
    # First, create stack representations of the characters in each of the two
    # input strings.
    s_stack = create_stack_representation(s)
    t_stack = create_stack_representation(t)

    # Using the stack representations created above, simply return whether the
    # two stack representations contain the same character elements.
    return s_stack == t_stack


class TestBackspaceCompareExamples(TestCase):
    """Test Backspace Compare Examples

    This test case includes all three of the examples from the problem
    description.
    """

    def test_example_one(self) -> None:
        self.assertTrue(backspace_compare("ab#c", "ad#c"))

    def test_example_two(self) -> None:
        self.assertTrue(backspace_compare("ab##", "c#d#"))

    def test_example_three(self) -> None:
        self.assertFalse(backspace_compare("a#c", "b"))


class TestFailedTestCases(TestCase):
    """Test Failed Test Cases"""

    def test_failed_test_case_one(self) -> None:
        self.assertFalse(backspace_compare("isfcow#", "isfco#w#"))
