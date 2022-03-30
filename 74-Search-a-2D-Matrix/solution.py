"""LeetCode Problem 74 - Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n
integer matrix matrix. This matrix has the following properties:

    * Integers in each row are sorted from left to right.
    * The first integer of each row is greater than the last integer of the
      previous row.

Constraints
===========
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 100
 * -104 <= matrix[i][j], target <= 104

"""

from typing import List

from pytest import fixture


def binary_search(numbers: List[int], target: int) -> bool:
    # Calculate the midpoint of the array to inspect whether the target value
    # is higher or lower, thus eliminating half of the array in a single
    # iteration.
    mid = len(numbers) // 2

    # If the midpoint of the array contains the target value, then we've hit
    # paydirt and we return true.
    if numbers[mid] == target:
        return True
    elif len(numbers) == 1:
        # If the midpoint is not equal to the target, and the list only has a
        # single value in it, then the target value is not in the array, so we
        # can return false.
        return False
    elif target < numbers[mid]:
        # Since we are still looking for the target in a list with more than a
        # single element, look for the target value in the bottom half of the
        # array, since the target was less than the midpoint, and the list is
        # sorted.
        return binary_search(numbers[:mid], target)
    elif target > numbers[mid]:
        # Likewise, since the target value was greater than the midpoint,
        # recursively search the top half of the array for the target value.
        return binary_search(numbers[mid:], target)
    
    # If we somehow hit this point, which we shouldn't, then the value was
    # clearly not in the list, and we can simply return false, although again,
    # we shouldn't have to.
    return False


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # The first thing we need to do is find the row where the target could be.
    # To do this, we iterate over the matrix row by row, since there isn't a
    # better way to do this.
    for row in matrix:
        # We are looking for the first row where the last element is greater
        # than the target. This is the only row where the target could possibly
        # be.
        if row[-1] >= target:
            # If we've found the candidate row, we simply return the result of
            # performing a binary search on the candidate row.
            return binary_search(row, target)
    
    # If we hit this point, it means that the target value was greater than all
    # of the rows in the entire matrix, so the target is obviously not in the
    # matrix.
    return False


@fixture
def single_digit_odd_numbers() -> List[int]:
    return [1, 3, 5, 7]


def test_binary_search_for_existing_elements(single_digit_odd_numbers: List[int]) -> None:
    for number in single_digit_odd_numbers:
        assert binary_search(single_digit_odd_numbers, number) == True


def test_binary_search_for_nonexisting_elements(single_digit_odd_numbers: List[int]) -> None:
    for number in range(0, 10, 2):
        assert binary_search(single_digit_odd_numbers, number) == False


def test_example_one() -> None:
    assert search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True


def test_example_two() -> None:
    assert search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False


def test_greater_than_or_equal() -> None:
    assert search_matrix([[1]], 1) == True
