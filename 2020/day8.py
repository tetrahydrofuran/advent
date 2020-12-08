from HandheldGameConsole import HandheldGameConsole

if __name__ == '__main__':
    console = HandheldGameConsole()

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
    print(program)
    print(console.determine_accumulator_before_repeated_loop(program))
