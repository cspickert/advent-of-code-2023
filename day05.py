from functools import reduce

import base


def parse_ints(text):
    return [int(value) for value in text.split()]


class Map:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def __getitem__(self, source):
        for dest_start, src_start, range_len in self.values:
            src_range = range(src_start, src_start + range_len)
            if source in src_range:
                return dest_start + source - src_start
        return source


class Solution(base.Solution):
    def load_data(self, input):
        def parse_map(text):
            lines = text.splitlines()
            return Map(
                name=lines[0].split()[0],
                values=[parse_ints(line) for line in lines[1:]],
            )

        sections = input.split("\n\n")
        seeds = parse_ints(sections[0].split(": ")[1])
        maps = [parse_map(section) for section in sections[1:]]
        return (seeds, maps)

    def get_location(self, maps, seed):
        return reduce(lambda result, map: map[result], maps, seed)

    def part1(self, data):
        seeds, maps = data
        return min(self.get_location(maps, seed) for seed in seeds)
