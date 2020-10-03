def checksum1(matrix):
    return sum(max(line) - min(line) for line in matrix)


def checksum2(matrix):
    # Brute force to find the divisible numbers; not sure if there's a great way to search this
    counter = 0
    for row in matrix:
        for i in range(len(row)):
            for j in range(len(row)):
                if i == j:  # Don't check self
                    continue
                if row[i] / row[j] == row[i] // row[j]:
                    counter += row[i] // row[j]
                    break
    return counter


if __name__ == '__main__':
    with open('files/2.txt') as f:
        input_ = f.readlines()
    input_ = [[int(j) for j in i.strip().split('\t')] for i in input_]

    assert checksum1([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18
    print('Part 1:', checksum1(input_))

    assert checksum1([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]) == 18
    print('Part 2:', checksum2(input_))
