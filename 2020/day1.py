def part1(inputs):
    for i, j in enumerate(inputs):
        for k in inputs[i:]:
            if j + k == 2020:
                return j * k


if __name__ == '__main__':
    with open('files/1.txt') as f:
        input_ = f.readlines()
        input_ = [int(i.strip()) for i in input_]
    print(part1(input_))
