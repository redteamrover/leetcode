"""LeetCode Problem 843 - Guess the Word

This is an interactive problem.

You are given an array of unique strings wordlist where wordlist[i] is six
letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. The guessed word should have
type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches
(value and position) of your guess to the secret word. Also, if your guess is
not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. At the end
of any number of calls, if you have made 10 or fewer calls to Master.guess and
at least one of these guesses was secret, then you pass the test case.

Constraints
===========
 * 1 <= wordlist.length <= 100
 * wordlist[i].length == 6
 * wordlist[i] consist of lowercase English letters.
 * All the strings of wordlist are unique.
 * secret exists in wordlist.
 * numguesses == 10

TODO: Implement deterministic solution.

"""

from copy import deepcopy
from random import choice
from string import ascii_lowercase
from typing import List, Text

from pytest import fixture


def matching_characters(first: Text, second: Text) -> int:
    matching_characters_ = 0

    for index, character in enumerate(first):
        if character == second[index]:
            matching_characters_ += 1

    return matching_characters_


class Master:
    def __init__(self, wordlist: List[Text], secret: Text) -> None:
        # Ensure that the secret word is actually in the word list.
        if secret not in wordlist:
            # If it isn't, raise an exception to let the user know this
            # configuration is invalid.
            raise Exception("The secret is not in the word list.")

        # Otherwise, simply initialize the class members.
        self._wordlist = wordlist
        self._secret = secret

    def guess(self, word: str) -> int:
        if word not in self._wordlist:
            return -1

        return matching_characters(word, self._secret)

    def wordlist(self) -> List[Text]:
        return self._wordlist


def generate_random_word() -> Text:
    return "".join(choice(ascii_lowercase) for _ in range(6))


def generate_random_wordlist(length: int = 100) -> List[Text]:
    wordlist = []

    while len(wordlist) < length:
        word = generate_random_word()

        if word not in wordlist:
            wordlist.append(word)

    return wordlist


def generate_random_master(length: int = 100) -> Master:
    wordlist = generate_random_wordlist(length)
    return Master(wordlist, choice(wordlist))


def find_word(wordlist: List[Text], master: 'Master') -> bool:
    candidates = deepcopy(wordlist)
    guesses = []

    for _ in range(10):
        candidate = choice(candidates)
        score = master.guess(candidate)
        guesses.append((candidate, score))

        if score == 6:
            return True

        for guess, score in guesses:
            candidates = list(filter(lambda word: matching_characters(word, guess) == score, candidates))

    return False


@fixture
def example_one_master() -> Master:
    return Master(["acckzz", "ccbazz", "eiowzz", "abcczz"], "acckzz")


def test_example_one(example_one_master: Master) -> None:
    assert example_one_master.guess("aaaaaa") == -1
    assert example_one_master.guess("acckzz") == 6
    assert example_one_master.guess("ccbazz") == 3
    assert example_one_master.guess("eiowzz") == 2
    assert example_one_master.guess("abcczz") == 4


@fixture
def example_two_master() -> Master:
    return Master(["hamada", "khaled"], "hamada")


def test_example_two(example_two_master: Master) -> None:
    assert example_two_master.guess("khaled") == 0
    assert example_two_master.guess("hamada") == 6


@fixture
def random_master() -> Master:
    return generate_random_master()


def test_random_master(random_master: Master) -> None:
    assert find_word(random_master.wordlist(), random_master) is True


class TestFailedTestCases:
    def test_case_one(self) -> None:
        master = Master(["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"], "ccoyyo")
        assert find_word(master.wordlist(), master) is True
