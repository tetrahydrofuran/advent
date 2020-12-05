def part1(inputs):
    for i, j in enumerate(inputs):
        for k in inputs[i:]:
            if j + k == 2020:
                return j * k


def part2(inputs):
    for i, n1 in enumerate(inputs):
        for j, n2 in enumerate(inputs[i:]):
            for k, n3 in enumerate(inputs[j:]):
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3


if __name__ == '__main__':
    with open('files/1.txt') as f:
        input_ = f.readlines()
        input_ = [int(i.strip()) for i in input_]
    print(part1(input_))
    print(part2(input_))
