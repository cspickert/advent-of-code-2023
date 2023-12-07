from collections import Counter

import base


class Solution(base.Solution):
    def __init__(self):
        self.card_mapping = {str(i): i for i in range(1, 10)} | {
            c: i for i, c in enumerate("TJQKA", start=10)
        }

    def load_data(self, input):
        return [
            (self.parse_hand(a), int(b))
            for a, b in [line.split() for line in input.splitlines()]
        ]

    def part1(self, data):
        return sum(i * bid for i, (_, bid) in enumerate(sorted(data), start=1))

    # Helpers

    def parse_hand(self, hand):
        return (
            tuple(sorted(Counter(hand).values(), reverse=True)),
            tuple(self.card_mapping[k] for k in hand),
        )
