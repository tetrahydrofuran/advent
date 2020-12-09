from typing import Sequence


class HandheldGameConsole:
    def __init__(self):
        self.accumulator = self.instruction_pointer = 0
        self.program = self.line_execution_count = []

    def load_program(self, program: Sequence[str]):
        """Loads sequence of commands and resets state."""
        self.program = program
        self.line_execution_count = [0 for i in range(len(self.program))]
        self.accumulator = self.instruction_pointer = 0

    def execute_program(self):
        """Generic program execution to end, returning final accumulator value."""
        terminate = False
        while not terminate:
            _, _, terminate = self.execute_next_command()
        return self.accumulator

    def execute_next_command(self):
        command = self.program[self.instruction_pointer]
        self.line_execution_count[self.instruction_pointer] += 1

        prior_acc = self.accumulator

        operation, value = command.strip().split(' ')
        value = int(value)
        {  # Map instruction to function
            'nop': self.nop,
            'acc': self.acc,
            'jmp': self.jmp
        }[operation.lower()](value)
        curr_acc = self.accumulator

        termination = self.instruction_pointer >= len(self.program)
        print(operation, value, '|', prior_acc, curr_acc, '|', termination)
        return prior_acc, curr_acc, termination

    def nop(self, value: int = 0):
        """No operation"""
        self.instruction_pointer += 1

    def acc(self, value: int):
        """Increment accumulator"""
        self.accumulator += value
        self.nop()

    def jmp(self, value: int):
        """Jump"""
        self.instruction_pointer += value

    # endregion

    def determine_accumulator_before_repeated_loop(self, program: Sequence[str]):
        # Probably should be renamed now that accommodates natural termination
        self.load_program(program)
        while max(self.line_execution_count) < 2:
            prior, curr, termination = self.execute_next_command()
            if termination:
                print('Program terminated naturally.')
                return curr, termination
        # noinspection PyUnboundLocalVariable
        return prior, termination  # Last instruction is technically second execution
