from typing import List, Tuple


def _prep(item: str) -> List[int]:
    """Strips trailing \n and splits the dimension values"""
    return [int(i) for i in item.strip().split('x')]


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
        dim = _prep(dim)
        running_total += get_surf_and_extra(*dim)
    return running_total


def part2(dimensions: List[str]) -> int:
    """
    Gets smallest perimeter and volume
    """
    running_total = 0
    for dim in dimensions:
        dim = _prep(dim)
        dim = sorted(dim)
        running_total += (dim[0] + dim[1]) * 2  # Sum 2 smallest dim-perimeter
        running_total += dim[0] * dim[1] * dim[2]  # Sum volume
    return running_total


if __name__ == '__main__':
    with open('files/2.txt') as f:
        input_ = f.readlines()
    print(part1(input_))
    print(part2(input_))
