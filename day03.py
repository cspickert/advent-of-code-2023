import re
from collections import defaultdict

import base


class Solution(base.Solution):
    def load_data(self, input):
        numbers = defaultdict(list)
        parts = {}
        for row, line in enumerate(input.splitlines()):
            for match in re.finditer(r"\d+|[^\d\.]+", line):
                match_str = match.group()
                try:
                    value = int(match_str)
                    numbers[row].append((value, match.span()))
                except ValueError:
                    value = match_str
                    parts[row, match.start()] = value
        return numbers, parts

    def part1(self, data):
        numbers, parts = data

        part_numbers = []
        for row in numbers:
            for number, col_span in numbers[row]:
                for adj_coords in self.get_all_adj_coords(row, col_span):
                    if adj_coords in parts:
                        part_numbers.append(number)
                        continue

        return sum(part_numbers)

    def part2(self, data):
        numbers, parts = data

        result = 0
        for part_coords, part in parts.items():
            if part != "*":
                continue
            part_row, part_col = part_coords

            adj_numbers = set()
            for adj_row, adj_col in self.get_all_adj_coords(
                part_row,
                (part_col, part_col + 1),
            ):
                for number, number_span in numbers[adj_row]:
                    if adj_col in range(*number_span):
                        adj_numbers.add(number)
                        continue

            if len(adj_numbers) == 2:
                a, b = adj_numbers
                result += a * b

        return result

    def get_all_adj_coords(self, row, col_span):
        start, end = col_span
        for col in range(start - 1, end + 1):
            yield (row - 1, col)
        yield row, start - 1
        yield row, end
        for col in range(start - 1, end + 1):
            yield row + 1, col
