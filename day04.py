import base


class Solution(base.Solution):
    def load_data(self, input):
        def parse_nums(text):
            return set(int(value) for value in text.split())

        return [
            (parse_nums(a), parse_nums(b))
            for a, b in [
                line.split(": ")[1].split(" | ") for line in input.splitlines()
            ]
        ]

    def part1(self, data):
        return sum(
            2 ** (len(have_winning_nums) - 1)
            if (have_winning_nums := have_nums & winning_nums)
            else 0
            for winning_nums, have_nums in data
        )

    def part2(self, data):
        card_counts = [1] * len(data)
        win_counts = [len(have_nums & winning_nums) for have_nums, winning_nums in data]
        for i, win_count in enumerate(win_counts):
            for j in range(i + 1, i + 1 + win_count):
                card_counts[j] += card_counts[i]
        return sum(card_counts)
