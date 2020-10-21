from typing import List
import itertools
import re

FORBIDDEN_STRINGS = ('ab', 'cd', 'pq', 'xy')


def naughty_nice_check(string: str) -> bool:
    """Checks vowel count, double letter, forbidden strings and returns whether or not sit satisfies conditions"""
    vowels = 0
    double_letters = 0
    forbidden_string = False
    last_letter = ''
    for i, letter in enumerate(string):
        vowels += 1 if letter in 'aeiou' else 0
        double_letters += 1 if letter == last_letter else 0
        if last_letter + letter in FORBIDDEN_STRINGS:
            forbidden_string = True
        last_letter = letter
    return vowels >= 3 and double_letters >= 1 and not forbidden_string


def part1(inputs: List[str]) -> int:
    satisfying = 0
    for s in inputs:
        satisfying += naughty_nice_check(s)
    return satisfying


def naughty_nice_check2(string: str) -> bool:
    """
    Uses regex to search all combinations of satisfying conditions; slow, but don't need to think too hard about it.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # All combinations of two letters, search for single-separated
    # has_double_doubles = False
    # for two_letter_combo in itertools.product(letters, letters):
    #     x, y = two_letter_combo
    #     if re.findall('{0}.*{0}'.format(x, y), string):
    #         has_double_doubles = True
    #         break
    has_double_doubles = any(
        re.findall('{0}.*{0}'.format(x + y), string) for x, y in itertools.product(letters, letters)
    )

    has_separated_letter = any(
        re.findall('{0}.{0}'.format(letter), string) for letter in letters
    )

    return has_double_doubles and has_separated_letter


def part2(inputs: List[str]) -> int:
    return sum(naughty_nice_check2(s) for s in inputs)


if __name__ == '__main__':
    with open('files/5.txt') as f:
        input_ = f.readlines()

    assert naughty_nice_check('ugknbfddgicrmopn')
    assert not naughty_nice_check('jchzalrnumimnmhp')
    assert not naughty_nice_check('haegwjzuvuyypxyu')
    assert not naughty_nice_check('dvszwmarrgswjxmb')

    assert naughty_nice_check2('xxyxx')
    assert naughty_nice_check2('qjhvhtzxzqqjkmpb')
    assert not naughty_nice_check2('uurcxstgmygtbstg')
    assert not naughty_nice_check2('ieodomkazucvgmuy')
    print(part1(input_))
    print(part2(input_))
