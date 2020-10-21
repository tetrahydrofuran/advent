from typing import List


def get_surf_and_extra(l: int, w: int, h: int) -> int:
    """Returns surface area + area of smallest side"""
    side1 = l * w
    side2 = l * h
    side3 = w * h
    smallest = min(side1, side2, side3)
    return smallest + 2 * (side1 + side2 + side3)


def part1(dimensions: List[str]) -> int:
    """
    Given list of dimensions, calculate needed wrapping area.
    """
    running_total = 0
    for dim in dimensions:
        dim = dim.strip().split('x')
        running_total += get_surf_and_extra(*(int(x) for x in dim))
    return running_total


if __name__ == '__main__':
    with open('files/2.txt') as f:
        input_ = f.readlines()
    print(part1(input_))
