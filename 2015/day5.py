from typing import List

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


if __name__ == '__main__':
    with open('files/5.txt') as f:
        input_ = f.readlines()

    assert naughty_nice_check('ugknbfddgicrmopn')
    assert not naughty_nice_check('jchzalrnumimnmhp')
    assert not naughty_nice_check('haegwjzuvuyypxyu')
    assert not naughty_nice_check('dvszwmarrgswjxmb')
    print(part1(input_))
