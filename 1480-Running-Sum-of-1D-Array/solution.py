"""LeetCode Problem 1480 - Running Sum of 1D Array

Given an array nums. We define a running sum of an array as follows.

    runningSum[i] = sum(nums[0]…nums[i])

Return the running sum of nums.
"""

from collections.abc import Iterable
from itertools import accumulate
from operator import add


def running_sum(numbers: Iterable[int]) -> Iterable[int]:
    return accumulate(numbers, add)


def all_elements_equal(actual: Iterable[int], expected: Iterable[int]) -> bool:
    for actual, expected in zip(actual, expected):
        if actual != expected:
            return False
    
    return True


def test_example_one() -> None:
    assert all_elements_equal(running_sum([1, 2, 3, 4]), [1, 3, 6, 10])


def test_example_two() -> None:
    assert all_elements_equal(running_sum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])


def test_example_three() -> None:
    assert all_elements_equal(running_sum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])
