from typing import Tuple
from collections import Counter


def move(coordinate: Tuple[int, int], direction: str) -> Tuple[int, int]:
    x, y = coordinate
    _ = x, y
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
    visited = get_visited_houses(directions)

    c = Counter(visited)
    return len(c)
    # return sum(i > 1 for i in c.values())  # Originally thought wanted houses visited more than once.


def get_visited_houses(directions):
    loc = (0, 0)
    visited = [loc]
    for step in directions:
        loc = move(loc, step)
        visited.append(loc)
    return visited


def part2(directions: str) -> int:
    """
    Same methodology as part1, but maintain two separate lists of coordinates
    """
    # Split into every other direction
    santa = directions[::2]
    robo = directions[1::2]
    all_visited = get_visited_houses(santa) + get_visited_houses(robo)

    return len(Counter(all_visited))


if __name__ == '__main__':
    with open('files/3.txt') as f:
        input_ = f.read()
    print(part1(input_))
    print(part2(input_))
