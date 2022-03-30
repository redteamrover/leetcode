"""LeetCode Problem 68 - Text Justification

Given an array of strings words and a width maxWidth, format the text such that
each line has exactly maxWidth characters and is fully (left and right)
justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line does not divide evenly between words, the empty
slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is
inserted between words.

Note
====
 * A word is as a character sequence consisting of non-space characters only.
 * Each word's length is guaranteed to be at least 1 and less than maxWidth+1.
 * The input array words contains at least one word.

"""

from enum import Enum, auto, unique
from typing import List, Text


@unique
class JustificationType(Enum):
    Left = auto()
    Center = auto()


class Line:

    def __init__(self) -> None:
        self._words = []
    
    def __bool__(self) -> bool:
        return len(self._words) > 0
    
    def __iadd__(self, word: Text) -> None:
        self._words.append(word)
        return self
    
    def __len__(self) -> int:
        return len(" ".join(self._words))
    
    def __str__(self) -> Text:
        return " ".join(self._words)
    
    def center_justify(self, padding_characters_needed: int) -> None:
        for i in range(padding_characters_needed):
            self._words[i % (len(self._words) - 1)] = self._words[i % (len(self._words) - 1)] + " "
    
    def left_justify(self, padding_characters_needed: int) -> None:
        self._words[-1] = self._words[-1] + (" " * padding_characters_needed)
    
    def add_justification_padding(self, max_width: int, justification_type: JustificationType = JustificationType.Center) -> None:
        # Check that the current line actually has words in it.
        if len(self._words) == 0:
            # If there aren't any words in this line, we don't have to do
            # anything.
            return

        # Calculate the number of padding characters that we need to add to the
        # current line.
        padding_characters_needed = max_width - len(self)

        # The justification strategy depends on several factors, although the
        # primary factor is which justification strategy was specified when the
        # function was called.
        if justification_type == JustificationType.Center:
            # According to the problem specification, if the line only has a
            # single word, it must be left justified, even if it would have
            # otherwise been center-justified.
            if len(self._words) == 1:
                # Left justify the line since it only has a single word in it.
                self.left_justify(padding_characters_needed)
            else:
                # Since the line has more than one word in it, we can go ahead
                # and center justify the line as intended.
                self.center_justify(padding_characters_needed)
        # If the function is called with left-justification as the
        # justification strategy, there are no other checks to carry out.
        elif justification_type == JustificationType.Left:
            # Simply left-justify the line.
            self.left_justify(padding_characters_needed)
        # There are no other valid justification strategies to check for, so if
        # the justification strategy wasn't specified above, we've hit an
        # error.
        else:
            # Raise an exception indicating that the justification strategy the
            # user requested does not actually exist.
            raise Exception(f"Invalid justification type: {justification_type}")


def justify_text(words: List[Text], max_width: int) -> List[Text]:
    # Initialize the list of lines that we will be returning.
    lines = []

    # Each line in the output will be constructed one at a time using an
    # instance of the line class, which defines convenience methods for easily
    # constructing the justified lines.
    line = Line()

    # Iterate over each word in the input list.
    for word in words:
        # The first case we need to test for is whether the length of the
        # current word is equal to the maximum length of the line. We also have
        # to check whether we have zero words in the current line, because if
        # we didn't, the line would obviously run over the maximum length.
        if len(line._words) == 0 and len(word) == max_width:
            # If this is the case, we can simply append the current word to the
            # output list directly, since no justification is needed for a
            # single word that is the same length as the maximum character size
            # of the line.
            lines.append(word)

            # Once we have appended the word to the output list, move on to the
            # next word in the input.
            continue
        # If the length of the current word, plus it's required minimum of a
        # single space, are longer than the maximum length, we need to wrap up
        # the current line we are working on before handling this word.
        elif len(line) + len(" ") + len(word) > max_width:
            # Wrap up things with the current line by justifying it with the
            # words it currently has.
            line.add_justification_padding(max_width)

            # Once the line has been properly justified, go ahead and append it
            # to the output list of lines.
            lines.append(str(line))

            # Having finished processing the previous line, reset the state by
            # re-initializing the line object to a brand new empty line.
            line = Line()
        
        # Having done all of the necessary pre-processing above, go ahead and
        # add the current word to the current line.
        line += word
    
    # Once we have finished iterating over all of the words in the input list,
    # check if the current line has any words in it. If it does, we need to
    # justify the line and add it to the output list.
    if len(line._words):
        # Since this is the last line, the problem specification states that we
        # need to left justify it, rather than center justify it.
        line.add_justification_padding(max_width, JustificationType.Left)

        # Once the line has been justified, go ahead and append it to the list
        # of lines.
        lines.append(str(line))

    # Finally, return the list of lines.
    return lines


def test_example_one() -> None:
    assert justify_text(["This", "is", "an", "example", "of", "text", "justification."], 16) == ["This    is    an", "example  of text", "justification.  "]


def test_example_two() -> None:
    assert justify_text(["What", "must", "be", "acknowledgment", "shall", "be"], 16) == ["What   must   be", "acknowledgment  ", "shall be        "]


def test_example_three() -> None:
    assert justify_text(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20) == ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "]


def test_single_word() -> None:
    assert justify_text(["Hello"], 16) == ["Hello           "]


class TestFailedTestCases:
    def test_failed_test_case_one(self) -> None:
        assert justify_text(["Listen", "to", "many,", "speak", "to", "a", "few."], 6) == ["Listen","to    ","many, ","speak ","to   a","few.  "]
