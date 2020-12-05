from collections import Counter


def clean_input(string):
    """
    Cleans input string to min, max, letter, password.
    """
    number, character, password = string.split(' ')
    min_, max_ = number.split('-')
    character = character[0]
    return int(min_), int(max_), character, password


def part1(inputs):
    """Letter frequency interpretation of password rules."""
    valid = 0
    for inp in inputs:
        mi, ma, ch, pw = clean_input(inp)
        c = Counter(pw)
        if mi <= c[ch] <= ma:
            valid += 1
    return valid


def part2(inputs):
    """Letter positioning interpretation of password rules."""
    valid = 0
    for inp in inputs:
        p1, p2, ch, pw = clean_input(inp)
        condition1 = pw[p1 - 1] == ch
        condition2 = pw[p2 - 1] == ch
        if condition1 != condition2:  # XOR
            valid += 1
    return valid


if __name__ == '__main__':
    with open('files/2.txt') as f:
        input_ = f.readlines()

    print(clean_input('1-3 a: abcde'))
    print(part1(input_))
    print(part2(input_))
