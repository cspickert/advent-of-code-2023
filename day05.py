from functools import reduce

import base


def parse_ints(text):
    return [int(value) for value in text.split()]


def range_and(a, b):
    # a & b
    max_min = max(a.start, b.start)
    min_max = min(a.stop, b.stop)
    return range(max_min, min_max)


def range_sub(a, b):
    # a - b
    overlap = range_and(a, b)
    if not overlap:
        return [a]
    left = range(a.start, overlap.start)
    right = range(overlap.stop, a.stop)
    return [x for x in [left, right] if x]


def range_coalesce(ranges):
    ranges = sorted([r for r in ranges if r], key=lambda r: (r.start, r.stop))
    result = [ranges[0]]
    for b in ranges[1:]:
        a = result.pop()
        if range_and(a, b) or a.stop == b.start:
            x = range(a.start, b.stop)
            result.append(x)
        else:
            result.extend((a, b))
    return result


class Map:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def map_value(self, input_value):
        for dest_start, src_start, range_len in self.values:
            src_range = range(src_start, src_start + range_len)
            if input_value in src_range:
                return dest_start + input_value - src_start
        return input_value

    def map_range(self, input_range):
        input_ranges = [input_range]
        output_ranges = []

        for dest_start, src_start, range_len in self.values:
            unmapped_input_ranges = []

            for input_range in input_ranges:
                src_range = range(src_start, src_start + range_len)

                src_range_overlap = range_and(src_range, input_range)
                if src_range_overlap:
                    mapped_start = src_range_overlap.start - src_start + dest_start
                    mapped_stop = src_range_overlap.stop - src_start + dest_start
                    output_ranges.append(range(mapped_start, mapped_stop))

                    sub_result = range_sub(input_range, src_range_overlap)
                    unmapped_input_ranges.extend(sub_result)

                else:
                    unmapped_input_ranges.append(input_range)

            input_ranges = unmapped_input_ranges

        output_ranges.extend(input_ranges)

        result = range_coalesce(output_ranges)
        return result


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
        return reduce(lambda result, next_map: next_map.map_value(result), maps, seed)

    def part1(self, data):
        seeds, maps = data
        return min(self.get_location(maps, seed) for seed in seeds)

    def part2(self, data):
        seed_data, maps = data
        all_ranges = [
            range(range_start, range_start + range_len)
            for range_start, range_len in [
                seed_data[i : i + 2] for i in range(0, len(seed_data), 2)
            ]
        ]

        for next_map in maps:
            mapped_ranges = []
            for next_range in all_ranges:
                mapped_ranges.extend(next_map.map_range(next_range))
            all_ranges = range_coalesce(mapped_ranges)

        result = min(all_ranges, key=lambda r: r.start).start
        return result
