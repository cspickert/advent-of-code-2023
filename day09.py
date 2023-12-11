import base


class Solution(base.Solution):
    def load_data(self, input):
        return [[int(value) for value in line.split()] for line in input.splitlines()]

    def part1(self, data):
        return sum(self.get_next_value(sequence) for sequence in data)

    def part2(self, data):
        pass

    # Helpers

    def get_next_value(self, sequence):
        if all(value == 0 for value in sequence):
            return 0
        diffs = self.get_diff_sequence(sequence)
        return sequence[-1] + self.get_next_value(diffs)

    def get_diff_sequence(self, sequence):
        return [b - a for a, b in zip(sequence, sequence[1:])]
