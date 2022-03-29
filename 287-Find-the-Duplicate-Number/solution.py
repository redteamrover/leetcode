"""LeetCode Problem 287 - Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only
constant extra space.
"""

from collections.abc import Callable, Iterable
from itertools import islice
from typing import List, Optional


def naive_find_duplicate(numbers: List[int]) -> int:
    """Find Duplicate Number Using Naive Solution

    This function iterates over all of the numbers in the list. On each
    iteration, a nested for loop iterates over all of the numbers in the list
    after the current number, checking whether there is a match.

    If there is, then the number must occur more than once in the list, and we
    simply return the number.

    The nested iteration over the list means that this algorithm has a
    quadratic runtime complexity, rendering it impractical for any real
    scenario.
    """
    for index, number in enumerate(numbers):
        for other_number in islice(numbers, index + 1, len(numbers)):
            if number == other_number:
                return number


def find_duplicate_with_set(numbers: Iterable[int]) -> int:
    # Initialize the set of numbers already seen.
    seen = set()

    # Iterate over all of the numbers we are given.
    for number in numbers:
        # If we have already seen the number, then we simply return the number,
        # as it is by definition the repeated number.
        if number in seen:
            return number

        # If we haven't seen this number yet, add it to the set of numbers we
        # have seen already and keep looking.
        seen.add(number)

    # The problem specifies that a solution is guaranteed to exist, so if we do
    # not find one, something has gone terribly wrong.
    raise Exception("No solution found.")


def find_duplicate_floyd(numbers: List[int]) -> int:
    # Initialize the pointers to the first element in the list.
    tortoise = numbers[0]
    hare = numbers[0]

    while True:
        tortoise = numbers[tortoise]
        hare = numbers[numbers[hare]]

        if tortoise == hare:
            break

    tortoise = numbers[0]

    while tortoise != hare:
        tortoise = numbers[tortoise]
        hare = numbers[hare]

    return hare


def find_duplicate_floyd2(numbers: List[int]) -> int:
    # Initialize the pointers, but this time give them a head start.
    tortoise = numbers[0]
    hare = numbers[numbers[0]]

    # Keep cycling through the list until the pointers meet.
    while tortoise != hare:
        # The slow pointer is incremented once.
        tortoise = numbers[tortoise]

        # The fast pointer is incremented twice.
        hare = numbers[numbers[hare]]

    # The following line causes execution to hang indefinitely.
    # tortoise = numbers[0]
    #
    # The tortoise must be reset to the beginning.
    tortoise = 0

    # Once the pointers meet again, return the start of the cycle.
    while tortoise != hare:
        # This time, only increment the pointers by one node each.
        tortoise = numbers[tortoise]
        hare = numbers[hare]

    # Return the number that starts the cycle in the list.
    return hare


def find_duplicate(numbers: Iterable[int], finder_method: Callable = find_duplicate_floyd2) -> int:
    return finder_method(numbers)


def test_example_one() -> None:
    assert find_duplicate([1, 3, 4, 2, 2]) == 2


def test_example_two() -> None:
    assert find_duplicate([3, 1, 3, 4, 2]) == 3


def test_simplest_case() -> None:
    assert find_duplicate([1, 1]) == 1


def test_multiple_repetitions_of_the_same_number() -> None:
    assert find_duplicate([2, 2, 2, 2, 2]) == 2
