from collections import Counter


def part1(paren):
    """
    +1 for open paren, -1 for close paren
    """
    c = Counter(paren)
    return c['('] - c[')']


if __name__ == '__main__':
    with open('files/1.txt') as f:
        input_ = f.read().strip()

    assert part1('(())()()') == 0
    assert part1(')())())') == -3
    print(part1(input_))
