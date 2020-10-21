from typing import Tuple
from collections import Counter


def move(coordinate: Tuple[int, int], direction: str) -> Tuple[int, int]:
    x, y = coordinate
    _ = x,y
    if direction == '>':
        x += 1
    elif direction == '<':
        x -= 1
    elif direction == '^':
        y += 1
    else:  # v
        y -= 1

    return x, y


def part1(directions: str) -> int:
    """
    Gets coordinates visited at least once by maintaining a list of each timestep.
    """
    loc = (0, 0)
    visited = [loc]
    for step in directions:
        loc = move(loc, step)
        visited.append(loc)

    c = Counter(visited)
    return len(c)
    # return sum(i > 1 for i in c.values())


if __name__ == '__main__':
    with open('files/3.txt') as f:
        input_ = f.read()
    print(part1(input_))
    # print(part2(input_))


