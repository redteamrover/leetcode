"""LeetCode Problem 31 - Next Permutation

A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of
arr:

        [1,2,3], [1,3,2], [3,1,2], [2,3,1].

The next permutation of an array of integers is the next lexicographically
greater permutation of its integer. More formally, if all the permutations of
the array are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in
the sorted container. If such arrangement is not possible, the array must be
rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

from typing import List, TypeVar


# Declare a generic type variable to allow static definition of generic
# functions.
T = TypeVar('T')


def swap(elements: List[T], a: int, b: int) -> None:
    """Swap Elements

    This utility function simply swaps the elements located at the indices
    specified by a and b.
    """
    temp = elements[a]
    elements[a] = elements[b]
    elements[b] = temp


def next_permutation(numbers: List[int]) -> None:
        """Next Permutation

        This function does not return anything. Instead, the permutations are
        done in-place.
        """
        # In order to rearrange the list into the next lexicographical
        # permutation, we need to find the first element from the end of the
        # list that is smaller than the element after it.
        #
        # To do this, we start searching from the second-to-last index in the
        # list, which is equal to the length of the list minus two.
        i = len(numbers) - 2

        # Continue searching while the current index is greater than or equal
        # to zero.
        while i >= 0:
            # Check if this element is smaller than the element after it.
            if numbers[i+1] > numbers[i]:
                # Now that we've found the element, we need to find the index
                # of the smallest element greater than this element that is
                # between this element and the end of the list.
                #
                # We first initialize the minimum to be the maximum of the
                # rest of the elements in the list, just to have something to
                # compare against.
                minimum = max(numbers[i+1:])
                location = None

                # Find the smallest element greater than this element to the
                # right of this element.
                for index, element in enumerate(numbers):
                    # Don't bother with the elements in the list to the left of
                    # this element (or with this element itself).
                    if index <= i:
                        continue

                    # If the current element is greater than our target element
                    # and less than or equal to the current minimum, we update
                    # the minimum and its index.
                    if element > numbers[i] and element <= minimum:
                        minimum = element
                        location = index

                # Once we have found the necessary elements, switch their
                # positions in the list.
                swap(numbers, i, location)

                # Finally, we need to reverse the order of the elements to the
                # right of the first decreasing element we found.
                j = i + 1
                k = len(numbers) - 1

                while j < k:
                    # Swap the two current elements.
                    swap(numbers, j, k)

                    # Increment and decrement the head and tail indicies,
                    # respectively.
                    j += 1
                    k -= 1
                
                # Once we have done all of the above, all we need to do is
                # return from the function. All of the swaps were done in-place
                # and therefore we don't actually need to return anything.
                return

            # We still haven't found an element smaller than the element after
            # it, so keep looking.
            i -= 1
        
        # If we get to this point, then we were never able to find a number
        # that was smaller than the one after it. Therefore, this permutation
        # of the elements in the list is the maximal possible lexicographical
        # permutation possible.
        #
        # Since this implies that the elements are arranged in descending
        # order, we simply reverse the list. We specifically do not sort it,
        # since the best possible sorting method will have a runtime complexity
        # of O(N*log(N)). Since we already know the elements are in reverse
        # order, simply reversing the elements requires only O(N) time.
        for i, j in zip(range(len(numbers)), reversed(range(len(numbers)))):
            # Continue swapping until the head and tail indices meet up.
            if j <= i:
                break

            # Swap the two current elements.
            swap(numbers, i, j)


def test_example_one() -> None:
    numbers = [1, 2, 3]
    next_permutation(numbers)
    assert numbers == [1, 3, 2]


def test_example_two() -> None:
    numbers = [3, 2, 1]
    next_permutation(numbers)
    assert numbers == [1, 2, 3]


def test_example_three() -> None:
    numbers = [1, 1, 5]
    next_permutation(numbers)
    assert numbers == [1, 5, 1]
    next_permutation(numbers)
    assert numbers == [5, 1, 1]
    next_permutation(numbers)
    assert numbers == [1, 1, 5]


def test_case_one() -> None:
    numbers = [1, 4, 2, 1]
    next_permutation(numbers)
    assert numbers == [2, 1, 1, 4]


def test_case_two() -> None:
    numbers = [9, 4, 2, 1 ,7, 6]
    next_permutation(numbers)
    assert numbers == [9, 4, 2, 6, 1, 7]


def test_case_three() -> None:
    numbers = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    next_permutation(numbers)
    assert numbers == [1, 5, 8, 5, 1, 3, 4, 6, 7]


if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5]
    permutations_list = permutations(elements)
    print(permutations_list)
