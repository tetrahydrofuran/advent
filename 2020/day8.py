from HandheldGameConsole import HandheldGameConsole

console = HandheldGameConsole()


def part1(program):
    return console.determine_accumulator_before_repeated_loop(program)[0]


def part2(program):
    """I don't know if there is a better way, but brute force loop all the JMP and NOP commands to check."""
    nop = ['nop' in command.lower() for command in program]
    jmp = ['jmp' in command.lower() for command in program]
    for i, replace in enumerate(nop):
        program_ = program.copy()
        program_[i] = program_[i].replace('nop', 'jmp') if replace else program_[i]
        acc, term = console.determine_accumulator_before_repeated_loop(program_)
        if term:
            return acc
    for i, replace in enumerate(jmp):
        program_ = program.copy()
        program_[i] = program_[i].replace('jmp', 'nop') if replace else program_[i]
        acc, term = console.determine_accumulator_before_repeated_loop(program_)
        if term:
            return acc


if __name__ == '__main__':
    test_program = '''
    nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''.strip().split('\n')
    # print(test_program)
    # print(console.determine_accumulator_before_repeated_loop(test_program))

    with open('files/8.txt') as f:
        program = f.readlines()
    # print(program)
    print('Part 1:', part1(program))
    print('Part 2:', part2(program))
