from day4 import get_passports as get_answers  # Same functionality


def part1(answers):
    return sum(len(set(group.replace(' ', ''))) for group in answers)


def part2(answers):
    pass


if __name__ == '__main__':
    with open('files/6.txt') as f:
        input_ = f.readlines()

    answer_sets = get_answers(input_)
    print(input_)
    print(answer_sets)
    print(part1(answer_sets))
    # print(part2(input_))
