import math

import base


class Solution(base.Solution):
    def part1(self, data):
        games = self.load_data_part1(data)
        return self.count_all_solutions(games)

    def part2(self, data):
        games = self.load_data_part2(data)
        return self.count_all_solutions(games)

    # Helpers

    def load_data_part1(self, input):
        return zip(
            *(
                [int(value) for value in line.split()[1:]]
                for line in input.splitlines()
            ),
        )

    def load_data_part2(self, input):
        return (tuple(int("".join(line.split()[1:])) for line in input.splitlines()),)

    def count_solutions(self, game):
        duration, distance = game

        # distance = hold_duration * (total_duration - hold_duration)
        # ...
        # 9 = x * (7 - x)
        # 9 = 7x - x^2
        # x^2 - 7x + 9 = 0
        #  a = 1, b = -7, c = 9
        # x = (-b +- sqrt(b**2-4ac)) / 2a

        hold_min = (duration - math.sqrt((-duration) ** 2 - 4 * distance)) / 2
        adj_hold_min = math.ceil(hold_min)
        if adj_hold_min == hold_min:
            adj_hold_min += 1

        hold_max = (duration + math.sqrt((-duration) ** 2 - 4 * distance)) / 2
        adj_hold_max = math.floor(hold_max)
        if adj_hold_max == hold_max:
            adj_hold_max -= 1

        return (adj_hold_max - adj_hold_min) + 1

    def count_all_solutions(self, games):
        return math.prod(self.count_solutions(game) for game in games)
