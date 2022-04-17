"""LeetCode Problem 1874 - Minimize Product Sum of Two Arrays

The product sum of two equal-length arrays a and b is equal to the sum of
a[i] * b[i] for all 0 <= i < a.length (0-indexed).

For example, if a = [1,2,3,4] and b = [5,2,3,1], the product sum would be
1*5 + 2*2 + 3*3 + 4*1 = 22.

Given two arrays nums1 and nums2 of length n, return the minimum product sum if
you are allowed to rearrange the order of the elements in nums1.

Constraints
===========
 * n == nums1.length == nums2.length
 * 1 <= n <= 10^5
 * 1 <= nums1[i], nums2[i] <= 100

"""

from math import prod as product
from typing import List


def minimize_product_sum(candidate_coordinates: List[int], target_vector: List[int]) -> int:
    """Minimize Product Sum

    The simplest way to solve this problem is to realize that the way to
    minimize the dot product of two vectors, assuming you can rearrange one of
    them, is by pairing the largest elements in the target vector with the
    smallest numbers in the candidate elements.

    In this function, we mutate both of the input vectors directly for
    convenience, but we could have easily simply copied the target vector.
    """
    candidate_coordinates.sort()
    target_vector.sort(reverse=True)
    return sum(map(product, zip(candidate_coordinates, target_vector)))


def test_example_one() -> None:
    """Test Case: Example One"""
    assert minimize_product_sum([5, 3, 4, 2], [4, 2, 2, 5]) == 40


def test_example_two() -> None:
    """Test Case: Example Two"""
    assert minimize_product_sum([2, 1, 4, 5, 7], [3, 2, 4, 8, 6]) == 65
