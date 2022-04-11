"""LeetCode Problem 3 - Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating
characters.

Constraints
===========
 * 0 <= s.length <= 5 * 10^4
 * s consists of English letters, digits, symbols and spaces.

"""

from typing import Callable, Text


def contains_repeated_characters(string: Text) -> bool:
    """Check Whether the Input String Contains Repeated Characters"""
    # Initialize the set of characters already seen.
    characters = set()

    # Iterate over each character in the input string.
    for character in string:
        # Check whether we have already seen the current character.
        if character in characters:
            # If we have, then this string contains repeated characters, and we
            # thus return true.
            return True
        
        # If we have not already seen the current character, add it to the set
        # of seen characters.
        characters.add(character)

    # If we reach this point, we did not find any repeated characters in the
    # input string, so we return false.
    return False


def naive_method(string: Text) -> int:
    """Naive Method for Calculating the Length of the Longest Substring

    This solution has a cubic runtime complexity, meaning O(N^3), because we
    have three nested for loops (including the one in the 'contains repeated
    characters' utility function defined above).

    This function is therefore too slow to be of any practical use in a real
    world scenario.
    """
    # Keep track of the maximum length we have seen so far.
    maximum_length = 0

    # Save the length of the input string for legibility.
    N = len(string)

    # Iterate over each character in the input string. This has the effect of
    # allowing us to iterate over all substrings that start on each character
    # of the input string.
    for i in range(N):
        # Iterate over all possible lengths of the substrings within the input
        # string, taking into account the fact that as we move forward in the
        # input string, the maximum possible length of the substring decreases,
        # as there are then less characters.
        for j in range(1, N - i + 1):
            # The substring currently under consideration starts at the index
            # demarcated by i and continues all the way up to (but not
            # including) the index demarcated by i + j.
            substring = string[i:i+j]

            # Check whether the current substring has any repeated characters.
            if not contains_repeated_characters(substring):
                # If it does not, update the maximum length we have encountered
                # so far.
                maximum_length = max(maximum_length, len(substring))

    # Once we have checked all of the possible substrings in the input string,
    # return the maximum length we found.
    return maximum_length


def state_machine(string: Text) -> int:
    """Length of Longest Substring"""
    # Initialize the maximum length variable which will track the maximum
    # length of a substring with no repeated characters we have seen so far.
    maximum_length = 0

    # Initialize the current length of the longest substring we have seen to
    # zero, since we haven't inspected anything yet.
    length = 0

    # Initialize the dictionary of characters we have seen. The keys of this
    # dictionary will be the characters themselves, while the values will be
    # the index of the character where we last saw it.
    characters_seen = {}

    # Begin iterating over the input string. We use the enumerate function here
    # in order to get both the index and the actual character value of the
    # element we are currently on.
    for index, character in enumerate(string):
        # First, check whether we have already seen the current character
        # before.
        if character in characters_seen:
            # Since we have already seen this character, we need to do a few
            # things. We begin by potentially preserving the current length, as
            # it could be the maximum length.
            maximum_length = max(maximum_length, length)

            # Second, rather than simply starting over, considering all of the
            # possible substrings beginning on at index after the offending
            # character, we simply trim the current substring under
            # consideration by removing the characters we saw prior to (and
            # including) the previous time we saw this character.
            for i in range(index - length, characters_seen[character] + 1):
                # Remove this character from the hash table of characters we
                # have already seen.
                del characters_seen[string[i]]

                # Adjust the length of the current substring under
                # consideration.
                length -= 1

            # Once the prior adjustments have been made, we simply continue
            # with the usual operations for a character we have not already
            # seen.
            #
            # Note that we also remove the character that triggered this
            # conditional block, so once this block has finished executed, we
            # technically haven't seen that character before.

        # Increment the current length of the substring under consideration.
        length += 1

        # Add the current character to the hash table of characters we have
        # already seen, using its value as the key and its index as the value.
        characters_seen[character] = index

    # Once we have finished processing the input string, update the maximum
    # length.
    #
    # We do this prior to removing characters from the 'characters seen' hash
    # table as well, but if the input string has no duplicate characters, the
    # maximum length would have otherwise never been updated.
    maximum_length = max(maximum_length, length)

    # Return the maximum length.
    return maximum_length


def length_of_longest_substring(string: Text, method: Callable[[Text], int] = state_machine) -> int:
    """Length of Longest Substring

    This function calculates the length of the longest substring in the input
    string without repeating characters.
    """
    return method(string)


class TestExamples:
    """Test Suite: LeetCode Examples"""
    def test_example_one(self) -> None:
        """Test Case: Example One"""
        assert length_of_longest_substring("abcabcbb") == 3

    def test_example_two(self) -> None:
        """Test Case: Example Two"""
        assert length_of_longest_substring("bbbbb") == 1

    def test_example_three(self) -> None:
        """Test Case: Example Three"""
        assert length_of_longest_substring("pwwkew") == 3


class TestHashTablePurge:
    """Test Suite: Hash Table Purge

    This test suite contains the test function(s) related to the removal of
    characters we have already seen while traversing the input string.
    """
    def test_minimum_removals(self) -> None:
        """Test Case: Minimum Removals

        This test case ensures that when we come across a character we have
        already seen, only the minimal number of removals are carried out,
        ensuring optimal performance under load.
        """
        assert length_of_longest_substring("abcabcd") == 4
        assert length_of_longest_substring("bacabcd") == 4
        assert length_of_longest_substring("abcabed") == 5
        assert length_of_longest_substring("zabcafed") == 6
        assert length_of_longest_substring(" zabcafed") == 6


class TestEdgeCases:
    """Test Suite: Edge Cases"""
    def test_empty_string(self) -> None:
        """Test Case: Empty String

        It is possible for the input string to be comprised of zero characters,
        so we need to ensure that this case is considered.
        """
        assert length_of_longest_substring("") == 0

    def test_simplest_string(self) -> None:
        """Test Case: Simplest String

        The simplest possible case is that of a string with a single character,
        so make sure that the solution correctly calculates its length to be
        one.

        This test case includes single character strings other than the letter
        a to cover non-obvious scenarios where the specific character matters,
        as well as a symbol and a space, to ensure that those characters (which
        are also valid) are accounted for as well.
        """
        assert length_of_longest_substring("a") == 1
        assert length_of_longest_substring("b") == 1
        assert length_of_longest_substring("z") == 1
        assert length_of_longest_substring("-") == 1
        assert length_of_longest_substring(" ") == 1
