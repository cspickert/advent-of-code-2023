import re

import base


class Solution(base.Solution):
    def load_data(self, input):
        numbers = []
        parts = {}
        for row, line in enumerate(input.splitlines()):
            for match in re.finditer(r"\d+|[^\d\.]+", line):
                match_str = match.group()
                try:
                    value = int(match_str)
                    numbers.append((value, row, match.span()))
                except ValueError:
                    value = match_str
                    parts[row, match.start()] = value
        return numbers, parts

    def part1(self, data):
        numbers, parts = data
        part_numbers = []
        for number, row, col_span in numbers:
            for adj_coords in self.get_all_adj_coords(row, col_span):
                if adj_coords in parts:
                    part_numbers.append(number)
                    continue
        return sum(part_numbers)

    def get_all_adj_coords(self, row, col_span):
        start, end = col_span
        for col in range(start - 1, end + 1):
            yield (row - 1, col)
        yield row, start - 1
        yield row, end
        for col in range(start - 1, end + 1):
            yield row + 1, col
