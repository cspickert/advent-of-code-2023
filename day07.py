from collections import Counter

import base


class Solution(base.Solution):
    def part1(self, data):
        hands = self.load_hands(data)
        return self.total_winnings(hands)

    def part2(self, data):
        hands = self.load_hands(data, jokers=True)
        return self.total_winnings(hands)

    # Helpers

    def total_winnings(self, hands):
        return sum(i * bid for i, (_, bid) in enumerate(sorted(hands), start=1))

    def load_hands(self, input, jokers=False):
        return [
            (self.parse_hand(a, jokers), int(b))
            for a, b in [line.split() for line in input.splitlines()]
        ]

    def parse_hand(self, hand, jokers):
        card_mapping = self.card_mapping(jokers)
        counts = Counter(hand)
        if jokers:
            try:
                (best_card, _), *_ = Counter(hand.replace("J", "")).most_common()
            except ValueError:
                best_card = "A"
            best_hand = hand.replace("J", best_card)
            counts = Counter(best_hand)
        return (
            tuple(value for _, value in counts.most_common()),
            tuple(card_mapping[k] for k in hand),
        )

    def card_mapping(self, jokers):
        card_mapping = {str(i): i for i in range(2, 10)} | {
            c: i for i, c in enumerate("TJQKA", start=10)
        }
        if jokers:
            card_mapping["J"] = 1
        return card_mapping
