"""LeetCode Problem 344 - Reverse String

Write a function that reverses a string. The input string is given as an array
of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Constraints
===========
 * 1 <= s.length <= 105
 * s[i] is a printable ascii character.

"""

from typing import List, Text


def reverse_string(string: List[Text]) -> None:
    """Reverse String

    This function reverses the input string in-place using only O(1) extra
    memory by allocating two index variables tracking the current location at
    both the head and the tail of the string.

    On each iteration, if the head index is less than the tail index, the
    characters at those positions are switched.
    """
    # Initialize the head index to the beginning position of the string.
    i = 0

    # Initialize the tail index to the last position in the string.
    j = len(string) - 1

    # Continue iteration over the input string until the head and the tail
    # indices either meet or pass one another.
    while i < j:
        # Swap the characters at the head and tail indices.
        t = string[i]
        string[i] = string[j]
        string[j] = t

        # Prepare for the next iteration by incrementing and decrementing the
        # head and tail indices, respectively.
        i += 1
        j -= 1


def test_example_one() -> None:
    string = ["h", "e", "l", "l", "o"]
    reverse_string(string)
    assert string == ["o", "l", "l", "e", "h"]


def test_example_two() -> None:
    string = ["H", "a", "n", "n", "a", "h"]
    reverse_string(string)
    assert string == ["h", "a", "n", "n", "a", "H"]


def test_single_character_string() -> None:
    string = ["A"]
    reverse_string(string)
    assert string == ["A"]
