def part1(input_map, slope=(3, 1)):
    input_map = [i.strip() for i in input_map]  # No strip lead to wraparound bug
    final_y = len(input_map)
    map_width = len(input_map[0])
    sx, sy = slope
    x = y = 0
    trees = 0
    print(input_map[0])
    while y < final_y - sy:
        x = (x + sx) % map_width
        y += sy
        _ = input_map[y].strip()
        trees += 1 if _[x] == '#' else 0

    return trees


def part2(input_map):
    def t(dx, dy):
        return part1(input_map, (dx, dy))

    i = t(1, 1)
    j = t(3, 1)
    k = t(5, 1)
    m = t(7, 1)
    n = t(1, 2)
    print(i, j, k, m, n)
    return i * j * k * m * n


if __name__ == '__main__':
    with open('files/3.txt') as f:
        input_ = f.readlines()
    print(part1(input_))
    print(part2(input_))
