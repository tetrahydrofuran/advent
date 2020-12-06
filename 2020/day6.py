from day4 import get_passports as get_answers  # Same functionality


def part1(answers):
    return sum(len(set(group.replace(' ', ''))) for group in answers)


def part2(raw_answers):
    """
    Get unanimous answers by taking the intersection of each answer group as they come.
    """
    unanimous_answers = 0
    group = None
    for line in raw_answers:
        if line != '\n':
            line = line.replace('\n', '')
            group = set(line) if group is None else group.intersection(line)
        else:
            unanimous_answers += len(group)
            group = None  # Reset the answer group
    unanimous_answers += len(group)
    return unanimous_answers


if __name__ == '__main__':
    with open('files/6.txt') as f:
        input_ = f.readlines()

    answer_sets = get_answers(input_)
    print(input_)
    print(answer_sets)
    print(part1(answer_sets))
    print(part2(input_))
