"""LeetCode Problem 680 - Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most
one character from it.

Constraints
===========
 * 1 <= s.length <= 10^5
 * string consists of lowercase English letters.

"""

from typing import Text


def is_valid_palindrome_with_possible_deletion(string: Text, deleted: bool = False) -> bool:
    """Is Valid Palindrome With Possible Deletion

    This function checks whether the input string is a palindromic string with
    at most one character deletion.
    """
    # Initialize the head index to the starting index in the input string,
    # and initialize the tail index to the last index in the input string.
    head = 0
    tail = len(string) -1

    # On each iteration, check whether the head and tail indices contain the
    # same character. If they do not, then we need to check whether removing
    # either the head or the tail characters yields a valid palindromic string.
    #
    # On the other hand, if the characters are the same, then we simply
    # increment the head index, decrement the tail index, and continue.
    while head < tail:
        # Check whether the head and tail indices contain different characters.
        if string[head] != string[tail]:
            # Check whether we have already deleted a character from the input
            # string.
            if deleted:
                # If we have already deleted a character from the input string,
                # then we can't just delete another one, so we return false
                # here.
                return False

            # If we haven't already deleted a character from the input string,
            # then we try that.
            if is_valid_palindrome_with_possible_deletion(string[head:tail], True) or is_valid_palindrome_with_possible_deletion(string[head+1:tail+1], True):
                # If removing either the head of the tail characters yielded a
                # palindromic string, then we return true.
                return True

            # If removing the head or the tail characters did not yield a
            # palindromic string, then we simply return false.
            return False

        # Otherwise, we simply increment the head index, decrement the tail
        # index, and we move on to the next iteration.
        head += 1
        tail -= 1

    # This is the best case scenario where all of the characters in the head
    # and tail indices matched up. Therefore, we have a palindromic string, and
    # thus we return true.
    return True


def test_example_one() -> None:
    assert is_valid_palindrome_with_possible_deletion("aba") is True


def test_example_two() -> None:
    assert is_valid_palindrome_with_possible_deletion("abca") is True


def test_example_three() -> None:
    assert is_valid_palindrome_with_possible_deletion("abc") is False


def test_single_character_string() -> None:
    assert is_valid_palindrome_with_possible_deletion("a") is True


def test_two_character_string() -> None:
    assert is_valid_palindrome_with_possible_deletion("aa") is True
    assert is_valid_palindrome_with_possible_deletion("ab") is True


def test_three_character_string() -> None:
    assert is_valid_palindrome_with_possible_deletion("aaa") is True
    assert is_valid_palindrome_with_possible_deletion("abb") is True
    assert is_valid_palindrome_with_possible_deletion("bab") is True
    assert is_valid_palindrome_with_possible_deletion("cba") is False


def test_four_character_string() -> None:
    assert is_valid_palindrome_with_possible_deletion("aaaa") is True
    assert is_valid_palindrome_with_possible_deletion("abba") is True
    assert is_valid_palindrome_with_possible_deletion("abaa") is True
    assert is_valid_palindrome_with_possible_deletion("abbb") is True
    assert is_valid_palindrome_with_possible_deletion("abbc") is False
    assert is_valid_palindrome_with_possible_deletion("acbc") is True
