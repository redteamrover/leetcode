"""LeetCode Problem 1423 - Maximum Points You Can Obtain From Cards

There are several cards arranged in a row, and each card has an associated
number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the
row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score
you can obtain.

Constraints
===========
 * 1 <= cardPoints.length <= 10^5
 * 1 <= cardPoints[i] <= 10^4
 * 1 <= k <= cardPoints.length

"""

from itertools import accumulate, chain, islice
from typing import Callable, Dict, List, Optional, Tuple


def incorrect_naive(card_points: List[int], k: int) -> int:
    """Maximum Score: Incorrect, Naive Implementation

    The maximum possible score of k-selections is equal to the sum of those k
    selections if and only if each of those k selections was maximized.

    Note that this function returns the wrong answer if a sacrificial selection
    is required.
    """
    # If the list is empty, return a score of zero, since we obviously can't
    # pick a card, and cards are worth at least one point.
    if not card_points or not k:
        return 0

    # Check whether the card at the beginning of the arrangement is worth more
    # points than the card at the end.
    if card_points[0] > card_points[-1]:
        # If it is, then select it and return its value plus the value of the
        # next selection.
        return card_points[0] + maximum_score(card_points[1:], k-1)

    # If the card at the beginning is less than the one at the end, then do the
    # same thing as above, but selecting the card at the end instead, along
    # with the sum of the next selection.
    #
    # Note that if the card at the beginning is equal to the card at the end,
    # then it doesn't matter which one we pick first, since this selection will
    # be available on the next selection event.
    return card_points[-1] + maximum_score(card_points[:-1], k-1)


def recursive_subproblem(card_points: List[int], k: int, cache: Optional[Dict[Tuple[Tuple[int, ...], int], int]] = None) -> int:
    """Maximum Score: Recursive Subproblem Solution

    This function returns the maximum score of two possible scenarios:

        1. The resulting score is maximized by taking the front card, or
        2. The resulting score is maximized by taking the back card.

    While similar in spirit to the incorrect naive implementation, this
    solution is different because it explicitly calculates both possibilities,
    rather than only one.

    This function therefore has a O(2^N) runtime complexity when implemented
    without any memoization.

    TODO: Figure out if the cache is actually even doing anything. I don't
    think it is, because the state is unique enough on each call that it's not
    actually helping.
    """
    # The base case for this recursion is whether there are cards left to pick
    # from or we have run out of selections to make.
    if not card_points or not k:
        return 0

    # Create a tuple of the function arguments to use as the hash table key.
    #
    # The key must be a tuple rather than a list because lists are mutable, and
    # they are thus not hashable.
    state = tuple((tuple(card_points), k))

    # If no cache object was supplied, we initialize one and use it for all of
    # the subcalls.
    if cache is None:
        cache = {}

    # Otherwise, check whether the cache contains elements already. If it does,
    # check whether the current scenario has already been cached.
    if not cache or state not in cache:
        # Cache the result of this selection for future reference, making sure
        # to pass in the cache for future use.
        cache[state] = max(
            card_points[0] + recursive_subproblem(card_points[1:], k-1, cache),
            card_points[-1] + recursive_subproblem(card_points[:-1], k-1, cache)
        )

    # Return the maximum of the two resulting scores, depending on whether it
    # is better to select the card in the front or the card in the back.
    return cache[state]


def simplified(card_points: List[int], k: int) -> int:
    """Maximum Score: Simplified Method

    This function's implementation rests on the idea that the maximum subarray
    possible from our k selections of front or back cards will be a subarray of
    length k composed of elements from only the front, only the back, or a
    combination thereof.
    """
    # This is the value we will update after calculating the point total for
    # each combination of selections.
    maximum_point_total = 0

    # Get the length of the arrangement of cards.
    N = len(card_points)

    # Iterate over the possible subarray selections.
    for i in range(k + 1):
        # Calculate the point total for each possible subarray.
        points = sum(card_points[:i] + card_points[-1:N-k-1+i:-1])

        # If the point total for the current subarray is greater than the
        # current maximum, update the current maximum.
        maximum_point_total = max(maximum_point_total, points)

    # Once we have calculated all of the possible point totals, return the
    # maximum point total.
    return maximum_point_total


def simplified_with_iterators(card_points: List[int], k: int) -> int:
    """Maximum Score: Simplified Method

    This function's implementation rests on the idea that the maximum subarray
    possible from our k selections of front or back cards will be a subarray of
    length k composed of elements from only the front, only the back, or a
    combination thereof.

    The only difference between this method and the previous one is that this
    implementation relies on the use of iterators, rather than list slicing.
    """
    # Get the length of the arrangement of cards.
    N = len(card_points)

    # If there is only one card in the list, we can simply return the value of
    # this single card.
    #
    # This check is here because if there are less than two cards in the deck,
    # the argument to the first call to islice below errors out.
    if N == 1:
        return card_points[0]

    # Return the maximum possible point total from any possible subarray
    # selection.
    return max(
        sum(
            chain(
                islice(card_points, 0, i),
                islice(card_points, N - k + i, None)
            )
        ) for i in range(k + 1)
    )


def precomputing(card_points: List[int], k: int) -> int:
    """Maximum Score: Precomputing Sums"""
    # Get the length of the arrangement of cards.
    N = len(card_points)

    # If there is only one card in the list, we can simply return the value of
    # this single card.
    #
    # This check is here because if there are less than two cards in the deck,
    # the argument to the first call to islice below errors out.
    if N == 1:
        return card_points[0]

    # Precompute the running sum of the head and tail of the card arrangement.
    head = [0] + list(accumulate(islice(card_points, 0, k)))
    tail = [0] + list(accumulate(islice(reversed(card_points), 0, k)))

    # Keep track of the maximum points total we have seen.
    maximum_points = 0

    # Iterate over all possible combinations of subarray selections from the
    # front and the back of the card arrangement.
    for i in range(k + 1):
        # The points total for this selection is equal to the points total of
        # cards we selected from the front plus the points total of cards we
        # selected from the back.
        points = head[i] + tail[k - i]

        # If necessary, update the current maximum.
        maximum_points = max(maximum_points, points)

    # Return the maximum points total.
    return maximum_points


def maximum_score(card_points: List[int], k: int, method: Callable[[List[int], int], int] = precomputing) -> int:
    """Maximum Score"""
    return method(card_points, k)


class TestExamples:
    """Test Suite: Program Description Examples"""
    def test_example_one(self) -> None:
        """Test Case: Example One"""
        assert maximum_score([1, 2, 3, 4, 5, 6, 1], 3) == 12

    def test_example_two(self) -> None:
        """Test Case: Example Two"""
        assert maximum_score([2, 2, 2], 2) == 4

    def test_example_three(self) -> None:
        """Test Case: Example Three"""
        assert maximum_score([9, 7, 7, 9, 7, 7, 9], 7) == 55


class TestEdgeCases:
    """Test Suite: Edge Cases"""
    def test_no_selections_left(self) -> None:
        """Test Case: No Selections Left

        If you have no selections to make, the returned score should be zero,
        regardless of the value of the cards in the arrangement.
        """
        assert maximum_score([1, 2, 3, 4, 5], 0) == 0

    def test_single_card(self) -> None:
        """Test Case: Single Card

        This test case is the degenerate case where the arrangement of cards we
        are given contains only a single card. In this case, the maximum value
        of our selection must be exactly equal to the point value of the only
        possible card we can pick.
        """
        assert maximum_score([1], 1) == 1
        assert maximum_score([2], 2) == 2

    def test_sacrificial_selection(self) -> None:
        """Test Case: Sacrificial Selection

        Naive implementations do not pass this test case, because the naive
        implementation does not take into account the possibility that a high
        value card may be selected only after first making a seemingly
        sub-optimal selection.
        """
        assert maximum_score([11,49,100,20,86,29,72], 4) == 232
