"""LeetCode Problem 59 - Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from
1 to n2 in spiral order.

Constraints
===========
 * 1 <= n <= 20

"""

from typing import Iterable, List


def create_matrix(n: int) -> List[List[int]]:
    """Create NxN Matrix"""
    return [[0 for i in range(n)] for i in range(n)]


def matrix_elements(n: int) -> Iterable[int]:
    """Matrix Elements Generator"""
    for i in range(1, n**2 + 1):
        yield i


def populate_matrix(n: int, matrix: List[List[int]]) -> None:
    """Populate the NxN Matrix in Spiral Order"""
    # These indices keep track of where in the matrix we are. Specifically,
    # which layer of the spiral we are in.
    top = 0
    bottom = 0
    right = 0
    left = 0

    # The for loop used to actually populate the matrix works by going in one
    # of four possible directions in a specific order. By definition, spiral
    # order is right, down, left, and up.
    directions = ["R", "D", "L", "U"]

    # This direction variable is simply an index into the directions array that
    # actually specifies which direction of the matrix we are currently
    # iterating over. After each iteration of the for loop, the direction index
    # is incremented by one and reduced modulo four.
    direction = 0

    # Get an iterator for the matrix elements.
    #
    # This is pretty dumb, because the for loop is already giving us the
    # right element we need, but since the for loop gives us one direction at a
    # time (we are populating more than one element per iteration of the outer
    # for loop), we need this here. This means that the outer loop needs
    # cleaning up, but I'm going to bed.
    #
    # TODO: Clean up the outer for loop iteration, removing unnecessary element
    elements = matrix_elements(n)

    # Begin the actual population of the matrix in spiral order.
    for element in matrix_elements(n):
        if directions[direction] == "R":
            for i in range(left, n - right):
                matrix[top][i] = next(elements)
            
            top += 1
        elif directions[direction] == "D":
            for i in range(top, n - bottom):
                matrix[i][n - right - 1] = next(elements)

            right += 1
        elif directions[direction] == "L":
            for i in range(n - right - 1, left - 1, -1):
                matrix[n - bottom - 1][i] = next(elements)

            bottom += 1
        elif directions[direction] == "U":
            for i in range(n - bottom - 1, top - 1, -1):
                matrix[i][left] = next(elements)

            left += 1
        
        # Once the current direction has been taken of, set the next direction
        # we will handle in the next iteration of the loop.
        direction = (direction + 1) % 4


def generate_matrix(n: int) -> List[List[int]]:
    """Generate NxN Matrix From 1 to N in Spiral Order"""
    # Create the matrix with the necessary dimensions.
    matrix = create_matrix(n)

    # Populate the matrix in spiral order.
    populate_matrix(n, matrix)

    # Once the matrix has been populated with the appropriate values, return
    # it.
    return matrix


def test_example_one() -> None:
    """Test Case: Problem Example One"""
    assert generate_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]


def test_example_two() -> None:
    """Test Case: Problem Example Two"""
    assert generate_matrix(1) == [[1]]
