import operator
from functools import reduce

import base


class Solution(base.Solution):
    def load_data(self, input):
        def parse_round(text):
            return {b: int(a) for a, b in [item.split() for item in text.split(", ")]}

        def parse_game(text):
            chunks = text.split(": ")
            game_id = int(chunks[0].split()[1])
            rounds = [parse_round(item) for item in chunks[1].split("; ")]
            return (game_id, rounds)

        return [parse_game(line) for line in input.splitlines()]

    def part1(self, data):
        return sum(
            game_id
            for game_id, game in data
            if all(
                amount <= {"red": 12, "green": 13, "blue": 14}[color]
                for game_round in game
                for color, amount in game_round.items()
            )
        )

    def part2(self, data):
        return sum(
            reduce(
                operator.mul,
                (
                    max(
                        amount
                        for game_round in game
                        for round_color, amount in game_round.items()
                        if round_color == color
                    )
                    for color in ["red", "green", "blue"]
                ),
            )
            for game_id, game in data
        )
