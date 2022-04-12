"""LeetCode Problem 289 - Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway
in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial
state: live (represented by a 1) or dead (represented by a 0). Each cell
interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

    1. Any live cell with fewer than two live neighbors dies as if caused by
       under-population.

    2. Any live cell with two or three live neighbors lives on to the next
       generation.

    3. Any live cell with more than three live neighbors dies, as if by
       over-population.

    4. Any dead cell with exactly three live neighbors becomes a live cell, as
       if by reproduction.

The next state is created by applying the above rules simultaneously to every
cell in the current state, where births and deaths occur simultaneously. Given
the current state of the m x n grid board, return the next state.

Constraints
===========
 * m == board.length
 * n == board[i].length
 * 1 <= m, n <= 25
 * board[i][j] is 0 or 1.

Follow-Up
=========
 * Could you solve it in-place? Remember that the board needs to be updated
   simultaneously: You cannot update some cells first and then use their
   updated values to update other cells.
 * In this question, we represent the board using a 2D array. In principle, the
   board is infinite, which would cause problems when the active area
   encroaches upon the border of the array (i.e., live cells reach the border).
   How would you address these problems?

"""

from copy import deepcopy
from typing import List

from pytest import FixtureRequest, fixture


# Create a type alias for the game grid.
Grid = List[List[int]]


def cell_neighbors(x: int, y: int, state: Grid) -> int:
    """Cell Neighbors

    Return the number of live cells in the Moore neighborhood of the cell at
    position (x, y).
    """
    # Calculate the height and the width of the grid.
    H = len(state)
    W = len(state[0])

    # The number of neighbors of the cell, defined as the number of living
    # cells within the cell's Moore neighborhood, starts out at zero while we
    # check each of the maximum possible eight cells.
    neighbors = 0

    # Iterate over the range [x - 1, x + 1], inclusive.
    for j in range(x - 1, x + 2):
        # If the x-coordinate of this cell's neighbor would have been negative
        # or would exceed the width of the board, then this cell obviously does
        # not have a neighbor at that location, and we can simply keep going.
        if j < 0 or j >= W:
            continue

        # Iterate over the range [y - 1, y + 1], inclusive.
        for i in range(y - 1, y + 2):
            # If the y-coordinate of this cell's neighbor would have been
            # negative or would exceed the height of the board, then this cell
            # obviously does not have a neighbor at that location, and we can
            # simply keep going.
            if i < 0 or i >= H:
                continue

            # A cell is not a neighbor of itself, so make sure not to count
            # the cell at this cell's coordinates.
            if j == x and i == y:
                continue

            # Check whether the position on the grid with the given coordinates
            # contains a living cell.
            if state[i][j]:
                # If the cell at the given x and y coordinates is alive,
                # increment this cell's number of neighbors.
                neighbors += 1

    # Return the total number of neighbors for this cell.
    return neighbors


def cell_alive(alive: bool, neighbors: int) -> bool:
    """Cell Alive

    This method contains the transition function definition for a cell within
    the grid.
    """
    # Check whether this cell is alive at the moment.
    if alive:
        # If the cell is alive and has less than two neighbors, this cell dies
        # from underpopulation.
        if neighbors < 2:
            return False

        # If this cell is alive and has two or three neighbors, it lives on.
        if neighbors == 2 or neighbors == 3:
            return True

        # If this cell is alive and has more than three neighbors, it dies off
        # due to overpopulation.
        if neighbors > 3:
            return False

    # If this cell is dead and has exactly three neighbors, it becomes a live
    # cell, as if by reproduction from its surrounding neighbors.
    if neighbors == 3:
        return True

    # If none of the cases above matched, then this cell is dead.
    return False


def next_state(state: Grid) -> Grid:
    """Next State

    Given the current state of the grid, return the next state of the board
    without mutating the current state variable.
    """
    # Create a deep copy of the current grid state. This allows for the quick
    # creation of a 2-dimensional matrix object with the exact size parameters
    # we need.
    evolution = deepcopy(state)

    # Iterate over each row in the current state matrix.
    for y, row in enumerate(state):
        # Iterate over each cell in the current row of the current state
        # matrix.
        for x, cell in enumerate(row):
            # Get the number of neighbors for this cell.
            neighbors = cell_neighbors(x, y, state)

            # Use the cell's current status and the number of neighbors it has
            # to determine its state in the next evolution of the system.
            evolution[y][x] = int(cell_alive(cell, neighbors))

    # Once all of the cells in the matrix have been updated, return the grid
    # for the next state of the system.
    return evolution


def evolve(current_state: Grid) -> None:
        """Evolve the Current State

        This function does not return anything. Instead, the reference variable
        containing the current state is mutated directly, and thus contains the
        updated state upon the return of this function.
        """
        # Since the previous state must be replaced in-place with the new state
        # of the grid, we must iterate over each individual row and column of
        # the input state and manually update the value.
        for y, row in enumerate(next_state(current_state)):
            for x, cell in enumerate(row):
                # Update this cell in the input state by overwriting it with
                # the corresponding value from the next state.
                current_state[y][x] = cell


@fixture
def ordinary_sample_A() -> Grid:
    return [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ]


class TestNeighbors:
    """Test Suite: Cell Neighbors"""
    def test_cell_neighbors_A1(self, ordinary_sample_A: FixtureRequest) -> None:
        """Test Case: Cell Neighbors for Ordinary Sample A"""
        assert cell_neighbors(0, 0, ordinary_sample_A) == 1
        assert cell_neighbors(1, 0, ordinary_sample_A) == 1
        assert cell_neighbors(2, 0, ordinary_sample_A) == 2

        assert cell_neighbors(0, 1, ordinary_sample_A) == 2
        assert cell_neighbors(1, 1, ordinary_sample_A) == 3
        assert cell_neighbors(2, 1, ordinary_sample_A) == 1

        assert cell_neighbors(0, 2, ordinary_sample_A) == 0
        assert cell_neighbors(1, 2, ordinary_sample_A) == 2
        assert cell_neighbors(2, 2, ordinary_sample_A) == 1


class TestCellTransitionFunction:
    """Test Suite: Cell Transition Function Tests"""
    def test_all_valid_cases_for_living_cell(self) -> None:
        """Test Case: All Valid Cases for Living Cell"""
        assert cell_alive(True, 0) == False
        assert cell_alive(True, 1) == False
        assert cell_alive(True, 2) == True
        assert cell_alive(True, 3) == True
        assert cell_alive(True, 4) == False
        assert cell_alive(True, 5) == False
        assert cell_alive(True, 6) == False
        assert cell_alive(True, 7) == False
        assert cell_alive(True, 8) == False

    def test_all_valid_cases_for_dead_cell(self) -> None:
        """Test Case: All Valid Cases for Dead Cell"""
        assert cell_alive(False, 0) == False
        assert cell_alive(False, 1) == False
        assert cell_alive(False, 2) == False
        assert cell_alive(False, 3) == True
        assert cell_alive(False, 4) == False
        assert cell_alive(False, 5) == False
        assert cell_alive(False, 6) == False
        assert cell_alive(False, 7) == False
        assert cell_alive(False, 8) == False 


class TestNextState:
    """Test Suite: Next State"""
    def test_simplest_possible_grid(self) -> None:
        """Test Case: Simplest Possible Grid"""
        # A single cell has no neighbors, so if it is dead, it should stay
        # dead.
        assert next_state([[0]]) == [[0]]

        # If it is alive, it should die.
        assert next_state([[1]]) == [[0]]


def test_example_one() -> None:
    """Test Case: Example One"""
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    evolve(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]


def test_example_two() -> None:
    """Test Case: Example Two"""
    board = [[1, 1], [1, 0]]
    evolve(board)
    assert board == [[1, 1], [1, 1]]
