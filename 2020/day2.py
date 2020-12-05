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
    valid = 0
    for inp in inputs:
        mi, ma, ch, pw = clean_input(inp)
        c = Counter(pw)
        if mi <= c[ch] <= ma:
            valid += 1
    return valid


if __name__ == '__main__':
    with open('files/2.txt') as f:
        input_ = f.readlines()

    print(clean_input('1-3 a: abcde'))
    print(part1(input_))
