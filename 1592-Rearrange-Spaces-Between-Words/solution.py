"""LeetCode Problem 1592 - Rearrange Spaces Between Words

You are given a string text of words that are placed among some number of
spaces. Each word consists of one or more lowercase English letters and are
separated by at least one space. It's guaranteed that text contains at least
one word.

Rearrange the spaces so that there is an equal number of spaces between every
pair of adjacent words and that number is maximized. If you cannot redistribute
all the spaces equally, place the extra spaces at the end, meaning the returned
string should be the same length as text.

Return the string after rearranging the spaces.

Constraints
===========
 * 1 <= text.length <= 100
 * text consists of lowercase English letters and ' '.
 * text contains at least one word.

"""

from typing import Text


def reorder_spaces(text: Text) -> Text:
    """Reorder Spaces"""
    # Get a list of the words in the input text.
    words = text.split()

    # Get the number of words in the input text.
    number_of_words = len(words)

    # Get the number of spaces in the input text.
    number_of_spaces = text.count(" ")

    # We need to first check that we are not dividing by zero in the code
    # below, so if the number of words is one, simply set the number of spaces
    # between to zero, and set the number of spaces after to be exactly equal
    # to the total number of spaces in the input string.
    if number_of_words == 1:
        spaces_between, spaces_after = 0, number_of_spaces
    # Otherwise, we are okay to continue calculating the number of spaces
    # in between words and at the end of the input string as normal.
    else:
        # Get the number of spaces that should go between each word, as well as
        # the number of leftover spaces that should go at the end of the text.
        spaces_between, spaces_after = divmod(number_of_spaces, number_of_words - 1)

    # Append the requisite number of spaces to each of the words in the input
    # text, except for the last one, since these are spaces that need to be
    # between words.
    for index, word in enumerate(words[:-1]):
        # We need the index of the current word in order to modify the word
        # element in the list itself, rather than the temporary value we
        # currently have access to.
        words[index] = word + (" " * spaces_between)

    # Append the necessary spaces after the words in the input text. In other
    # words, add the spaces after the last word.
    words[-1] = words[-1] + (" " * spaces_after)

    # Return the words as a single text string by joining them using an empty
    # string between each word in the list.
    return "".join(words)


def test_single_word() -> None:
    """Test Case: Single Word"""
    assert reorder_spaces("word") == "word"
    assert reorder_spaces(" word") == "word "
    assert reorder_spaces("word ") == "word "


def test_two_words() -> None:
    """Test Case: Two Words"""
    assert reorder_spaces("word word") == "word word"
    assert reorder_spaces(" word word") == "word  word"
    assert reorder_spaces(" word word ") == "word   word"


def test_examples() -> None:
    """Test Case: Problem Description Examples"""
    assert reorder_spaces("  this   is  a sentence ") == "this   is   a   sentence"
    assert reorder_spaces(" practice   makes   perfect") == "practice   makes   perfect "
