"""LeetCode Problem 1 - Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""

from collections.abc import Iterable
from typing import Dict, List


def two_sum(numbers: Iterable[int], target: int) -> List[int]:
    # Initialize the lookup table.
    cache: Dict[int, int] = {}

    for index, value in enumerate(numbers):
        # Check whether we've already seen the value we need.
        if target - value in cache:
            # If it is, return our answer as a two-element list.
            return [cache[target - value], index]

        # Cache each element in the table, using its index as its value.
        cache[value] = index


def test_example_one() -> None:
    indices = two_sum([2, 7, 11, 15], 9)
    assert indices == [0, 1] or indices == [1, 0]


def test_example_two() -> None:
    indices = two_sum([3, 2, 4], 6)
    assert indices == [1, 2] or indices == [2, 1]


def test_example_three() -> None:
    indices = two_sum([3, 3], 6)
    assert indices == [0, 1] or indices == [1, 0]
