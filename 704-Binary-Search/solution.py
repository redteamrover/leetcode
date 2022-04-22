"""LeetCode Problem 704 - Binary Search

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints
===========
 * 1 <= nums.length <= 10^4
 * -10^4 < nums[i], target < 10^4
 * All the integers in the numbers array are unique.
 * The numbers list is sorted in ascending order.

"""

from typing import Callable, List

from pytest import FixtureRequest, fixture


def binary_search(numbers: List[int], target: int) -> int:
    """Binary Search

    Return the index of the target value within the numbers array, if it is
    present. If it isn't, the function returns -1.
    """
    # Cache the length of the input array.
    n = len(numbers)

    # Initialize the index variables to track the subset of the array we are
    # currently on.
    low = 0
    high = n

    # Continue iterating until the low index is greater than the high index, or
    # the high index is less than the low index.
    #
    # In either case, this means the target value is not in the numbers array.
    while low <= high:
        # Calculate the midpoint of the current subset of the array we are
        # currently on.
        mid = (high + low) // 2

        # Ensure that we do not trigger a segmentation fault if the midpoint is
        # out of range.
        if mid < 0 or mid >= n:
            # Since the midpoint is out of range, the value can't be in the
            # array.
            return -1

        # If the midpoint of this subsection contains the target value, we're
        # done looking.
        if target == numbers[mid]:
            # All that's left to do is to return the index where the value was
            # found.
            return mid
        # If the target value is less than the value at the midpoint, eliminate
        # half of the elements in the current subsection of the array by moving
        # the high index down.
        elif target < numbers[mid]:
            high = mid - 1
        # If the target value is greater than the value at the midpoint,
        # eliminate half of the elements in the current subsection of the array
        # by moving the low index up.
        elif target > numbers[mid]:
            low = mid + 1

    # If we hit this point, the target value was just not in the array, so we
    # return -1 as a sentinel value indicating the target value was not found.
    return -1


def search(numbers: List[int], target: int, method: Callable[[List[int], int], int] = binary_search) -> int:
    """Search

    Look for the target value within the numbers input list by calling the
    given method. If no method is specified, binary search is used by default.
    """
    return method(numbers, target)


@fixture
def example_list() -> List[int]:
    return [-1, 0, 3, 5, 9, 12]


def test_example_one(example_list: FixtureRequest) -> None:
    """Test Case: Example One"""
    assert search(example_list, 9) == 4


def test_example_two(example_list: FixtureRequest) -> None:
    """Test Case: Example Two"""
    assert search(example_list, 2) == -1


def test_target_greater_than_maximal_element() -> None:
    """Test Case: Target Greater Than Maximal Element

    Ensure that the search function works as expected when the target value is
    not in the array and is greater than all of the elements in the input
    array.
    """
    assert search([-1, 0, 3, 5, 9, 12], 13) == -1
