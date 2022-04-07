"""LeetCode Problem 1046 - Last Stone Weight

You are given an array of integers stones where stones[i] is the weight of the
ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two
stones and smash them together. Suppose the heaviest two stones have weights x
and y with x <= y. The result of this smash is:

        * If x == y, both stones are destroyed, and
        * If x != y, the stone of weight x is destroyed, and the stone of
          weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones
left, return 0.

Constraints
===========
 * 1 <= stones.length <= 30
 * 1 <= stones[i] <= 1000

"""

from dataclasses import dataclass, field
from heapq import heapify, heappop, heappush
from itertools import combinations
from typing import Callable, List


def naive_solution(weights: List[int]) -> int:
    """Naive Solution"""

    while len(weights) > 1:
        heavy = (None, None)
        light = (None, None)

        for i, a in enumerate(weights):
            if heavy[1] is None:
                heavy = (i, a)
                continue
            
            if a > heavy[1]:
                heavy = (i, a)

        for j, b in enumerate(weights):
            if light[1] is None:
                light = (j, b)
                continue

            if b > light[1] and j != heavy[0]:
                light = (j, b)
        
        heavy = (heavy[0], heavy[1] - light[1])
        weights[heavy[0]] = heavy[1]
        weights.pop(light[0])
    
    return weights[0] if weights else 0


@dataclass(order=True)
class Stone:
    index: int = field(compare=False)
    weight: int


def use_priority_queue(weights: List[int]) -> int:
    """Use Priority Queue

    This solution implements a priority queue for the easy accessing of the top
    two heaviest stones we currently have.

    TODO: Since the problem doesn't require the index, remove it from the class
    """
    # Make a list of all of the stones we have.
    #
    # Note that the list is constructed right away using a list comprehension
    # rather than using a generator expression because the heapify function
    # requires a list and not simply an iterable object.
    #
    # In addition, the weights of the stones are made negative to take
    # advantage of the standard library's heapq module, which only provides a
    # min-heap.
    stones = [Stone(index, -weight) for index, weight in enumerate(weights)]

    # Construct a heap in linear time via a call to the heapify function from
    # the standard library's heapq module.
    heapify(stones)

    # Continue smashing stones together until we have less than two stones
    # remaining.
    while len(stones) > 1:
        # Get the two heaviest stones we currently have.
        heavy = heappop(stones)
        light = heappop(stones)

        # If the two heaviest stones were the same weight, then they were both
        # destroyed in the collision.
        if heavy.weight == light.weight:
            # Since both stones weighed the same amount, we can just move on.
            continue
        
        # The lighter stone was completely destroyed, but the heavier stone is
        # still intact, albeit at least a little lighter.
        result = Stone(heavy.index, heavy.weight - light.weight)

        # Add the resulting stone to the collection of stones we currently
        # have.
        heappush(stones, result)

    # Return the weight of the remaining stone, if there is one. If there are
    # no remaining stones, return zero.
    return -heappop(stones).weight if stones else 0


def last_stone_weight(weights: List[int], method: Callable[[List[int]], int] = use_priority_queue) -> int:
    """Last Stone Weight"""
    return method(weights)


def test_example_one() -> None:
    """Test Case: Example One"""
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1


def test_example_two() -> None:
    """Test Case: Example Two"""
    assert last_stone_weight([1]) == 1
