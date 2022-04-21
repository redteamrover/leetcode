"""LeetCode Problem 705 - Design HashSet

Design a HashSet without using any built-in hash table libraries. Specifically,
implement the HashSet class:

    * void add(key) Inserts the value key into the HashSet.
    * bool contains(key) Returns whether the value key exists in the HashSet or not.
    * void remove(key) Removes the value key in the HashSet. If key does not exist in
      the HashSet, do nothing.

Constraints
===========
 * 0 <= key <= 10^6
 * At most 10^4 calls will be made to add, remove, and contains.

"""

from array import array


class HashSet:
    """Hash-based Set Class"""

    def __init__(self, *, capacity: int = 8) -> None:
        """Set Constructor

        Args:
            capacity: The size of the underlying array used to hold the hashtable
            buckets.

        TODO: Implement the set constructor.
        """
        # Initialize the set capacity.
        # TODO: Is this necessary?
        # self._capacity = capacity

        # Initialize the underlying array of items.
        self._items = array("B", [0 for _ in range(10**6 + 2)])

        # Initialize the set with a size of zero.
        self._size = 0

    def __contains__(self, item: int) -> bool:
        """Check whether the set contains the given item."""
        return self._items[item] != 0

    def __len__(self) -> int:
        """Return the size of the set."""
        return self._size

    def add(self, item: int) -> None:
        """Add an item to the set."""
        # If the item was not already in the set, increment the size of the set.
        if not self._items[item]:
            self._size += 1

        # Add the item to the set by setting its index to one.
        self._items[item] = 1

    def remove(self, item: int) -> None:
        """Remove an item from the set."""
        # If the item is actually in the set, decrement the size of the set.
        if self._items[item]:
            self._size -= 1

        # Remove the item from the set by setting its index to zero.
        self._items[item] = 0

    def contains(self, item: int) -> bool:
        """Check whether this set instance contains an item."""
        return item in self
