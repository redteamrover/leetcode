"""LeetCode Problem 11 - Container With Most Water

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints
===========
 * n == height.length
 * 2 <= n <= 10^5
 * 0 <= height[i] <= 10^4

"""

from collections import namedtuple
from pprint import pprint
from typing import Callable, List


# Reify the container column into its own data type.
ContainerColumn = namedtuple('ContainerColumn', ['index', 'height'])


def area(a: ContainerColumn, b: ContainerColumn) -> int:
    # The container can only be filled up to the height of the smaller
    # column, so use the minimum of the two heights as the height of
    # the container.
    height = min(a.height, b.height)
    
    # The width of the container is equal to the absolute value of the
    # difference of the indexes of the columns.
    width = abs(b.index - a.index)

    # Return the calculated area of the container.
    return width * height


def naive_solution(heights: List[int]) -> int:
    # Initialize the current maximum area of the container to zero.
    maximum = 0

    # The maximum area of any possible container is equal to the width between
    # the container columns, inidicated by the absolute difference in the
    # indices of the column heights, times the minimum of the two column
    # heights, for any given column combination.
    for index_a, height_a in enumerate(heights):
        for index_b, height_b in enumerate(heights):
            # We need two separate columns to make a container, so don't waste
            # time considering a container of width zero.
            if index_a == index_b:
                continue
            
            # The width of the container is equal to the absolute value of the
            # difference of the indexes of the columns.
            width = abs(index_a - index_b)

            # The container can only be filled up to the height of the smaller
            # column, so use the minimum of the two heights as the height of
            # the container.
            height = min(height_a, height_b)

            # Calculate the area of the container, assuming an area of zero for
            # the columns that could potentially be taking up space within the
            # walls of the container.
            area = width * height

            # If the area of the current container is greater than the current
            # maximum, we have a new maximum.
            if maximum < area:
                # Replace the current maximum with the area of the current
                # container.
                maximum = area

    # Once we have checked all of the possible combinations of column walls,
    # return the maximum area.
    return maximum


def linear_time(heights: List[int]) -> int:
    # Initialize the head index to the front of the list and the tail index to
    # the back of the list.
    head = 0
    tail = len(heights) - 1

    # Initialize the current maximum area of the container to zero.
    maximum_area = 0

    # Continue incrementing and decrementing the head and tail indices,
    # respectively, until they meet or pass one another.
    while head < tail:
        # At the start of each iteration, the left column of the container is
        # defined to be the column at the left index, with the corresponding
        # height, and the right column is likewise defined for the tail index.
        left_column = ContainerColumn(head, heights[head])
        right_column = ContainerColumn(tail, heights[tail])

        # Calculate the area of the current container using the left and right
        # columns.
        current_area = area(left_column, right_column)

        # If the current area of the container is greater than the current
        # maximum, replace the current maximum.
        maximum_area = max(maximum_area, current_area)
        
        # Since the height of the container is equal to the height of the
        # shorter column, the index we increment or decrement depends on which
        # column height is greater.
        #
        # If the left column is shorter than the right column, we move the head
        # index forward. If the height of the right column is greater than or
        # equal to the height of the left column, we move the tail pointer
        # towards the head pointer by one.
        if left_column.height < right_column.height:
            head += 1
        else:
            tail -= 1
    
    # Once the head and tail indices have met up or passed one another, we have
    # processed all of the relevant columns, so we simply return the maximum
    # area.
    return maximum_area


def max_area(heights: List[int], method: Callable = linear_time) -> int:
    """Max Area
    
    This function uses the specified method to calculate the maximum area of a
    container given the list of column heights.
    """
    return method(heights)


def test_example_one() -> None:
    """Test Case: Example One"""
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_two() -> None:
    """Test Case: Example Two"""
    assert max_area([1, 1]) == 1


def test_case_zero_heights() -> None:
    """Test Case: Zero Heights

    The heights of the columns can be zero, so it's important to make sure that
    we take this into account.
    """
    assert max_area([0, 0]) == 0


def test_case_no_valid_container() -> None:
    """Test Case: No Valid Container

    Make sure that a container with columns of height zero, one, and zero
    yields a maximum area of zero, since this means we effectively have a
    single wall for the container.
    """
    assert max_area([0, 1, 0]) == 0


def test_case_middle_container_valid() -> None:
    """Test Case: Middle Container is Valid

    In the previous test case, the middle column did not yield a valid
    container. Therefore, make sure if a middle container is possible, we test
    for that.
    """
    assert max_area([0, 1, 1, 0]) == 1


def test_case_uneven_columns() -> None:
    """Test Case: Uneven Columns

    While the column heights do not allow for a container with even walls, it
    does allow for a container, so make sure this checks out.
    """
    assert max_area([0, 3, 1]) == 1


def test_case_interleaved_columns() -> None:
    """Test Case: Interleaved Columns

    Make sure that container columns containing shorter columns still yield a
    correct volume for the contained fluid.
    """
    assert max_area([0, 3, 1, 2]) == 4
