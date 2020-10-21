from collections import Counter


def part1(paren: str) -> int:
    """
    Bulk calculation +1 for open paren, -1 for close paren
    """
    c = Counter(paren)
    return c['('] - c[')']


def part2(paren: str) -> int:
    """
    Take iterable approach to counting floors, break when -1
    """
    floor = 0
    for i, p in enumerate(paren):
        floor += 1 if p == '(' else -1
        if floor == -1:
            return i + 1  # 1-indexed position
    # Assume will always enter the basement


if __name__ == '__main__':
    with open('files/1.txt') as f:
        input_ = f.read().strip()

    assert part1('(())()()') == 0
    assert part1(')())())') == -3
    print(part1(input_))
    print(part2(input_))
