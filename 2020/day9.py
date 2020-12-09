def check_satisfy_preamble(number, preamble):
    """
    Brute forces the list of preceding numbers, returning True if a satisfying sum is found.
    """
    check = [i for i in preamble if i < number]
    # print(number, preamble, check)
    for i, num in enumerate(check):
        for num2 in check[i:]:
            if num + num2 == number:
                # print(number, num, num2, preamble)
                return True
    # print(number, preamble)
    return False


def part1(sequence, preamble_length, nth_not_satisfying=1):
    for i in range(len(sequence) - preamble_length - 1):
        number = sequence[i + preamble_length]
        preamble = sequence[i:i + preamble_length]

        satisfied = check_satisfy_preamble(number, preamble)
        print(number, preamble, satisfied)
        if not satisfied:
            print(number)
        nth_not_satisfying -= 1 if not satisfied else 0
        if nth_not_satisfying == 0:
            return number


def part2(target, sequence):
    """
    Add numbers until greater than target, then start dropping from the start of list.
    Repeat, unless target found.
    """
    running_total = 0
    things = []
    for i, num in enumerate(sequence):
        if num == target:
            break  # Means have reached the target number and messed up somewhere
        s = sum(things)
        if s == target:
            print('Range found:', min(things), max(things), things)
            return min(things) + max(things)
        else:
            things.append(num)
            s = sum(things)
            # print(s, things)
            while sum(things) > target:
                things.pop(0)  # Remove from beginning


if __name__ == '__main__':
    with open('files/9.txt') as f:
        code = f.readlines()
    code = [int(i.strip()) for i in code]
    # invalid = part1(code, 25, 1)  # 105950735
    invalid = 105950735
    # print(invalid)
    print(part2(invalid, code))
    test_code = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    # print(part1(test_code, 5, 1))  # 127
    print(part2(127, test_code))
