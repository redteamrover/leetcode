"""LeetCode Problem 905 - Sort Array by Parity

Given an integer array nums, move all the even integers at the beginning of the
array followed by all the odd integers.

Return any array that satisfies this condition.

Constraints
===========
 * 1 <= nums.length <= 5000
 * 0 <= nums[i] <= 5000

"""

from itertools import chain
from typing import Iterable, List


def is_even(number: int) -> bool:
    """Return true if the given integer is evenly divisible by two."""
    return number % 2 == 0


def is_odd(number: int) -> bool:
    """Return true if the given integer is not evenly divisible by two."""
    return is_even(number) == False


def even_numbers(numbers: Iterable[int]) -> Iterable[int]:
    """Return all of the even numbers in a given iterable."""
    return filter(is_even, numbers)


def odd_numbers(numbers: Iterable[int]) -> Iterable[int]:
    """Return all of the odd numbers in a given iterable."""
    return filter(is_odd, numbers)


class Solution:
    """Solution to LeetCode Problem 905 - Sort Array by Parity"""

    def sortArrayByParity(self, numbers: List[int]) -> List[int]:
        """Sort Array by Parity

        Given an integer array nums, move all the even integers at the beginning
        of the array followed by all the odd integers.
        """
        return list(chain(even_numbers(numbers), odd_numbers(numbers)))
