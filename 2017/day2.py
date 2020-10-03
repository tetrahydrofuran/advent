def checksum1(matrix):
    return sum(max(line) - min(line) for line in matrix)


if __name__ == '__main__':
    with open('files/2.txt') as f:
        input_ = f.readlines()
    input_ = [[int(j) for j in i.strip().split('\t')] for i in input_]

    assert checksum1([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18
    print('Part 1:', checksum1(input_))
