import math
from heapq import heappop, heappush

import base


class Solution(base.Solution):
    def load_data(self, input):
        return input.splitlines()

    def part1(self, data):
        distances = self.get_distances(data)
        return max(distances.values())

    def part2(self, data):
        pass

    # Helpers

    def get_distances(self, data):
        start = self.find_start(data)
        distances = {start: 0}
        queue = [(0, start)]
        while queue:
            dist, coords = heappop(queue)
            for next_coords in self.get_next_coords(data, coords):
                next_dist = dist + 1
                if next_coords not in distances or next_dist < distances[next_coords]:
                    distances[next_coords] = next_dist
                    heappush(queue, (next_dist, next_coords))
        return distances

    def find_start(self, data):
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == "S":
                    return row, col

    def get_next_coords(self, data, coords):
        for row, col in self.get_next_coords_raw(data, coords):
            if row in range(len(data)) and col in range(len(data[row])):
                if data[row][col] not in "S.":
                    yield row, col

    def get_next_coords_raw(self, data, coords):
        r, c = coords
        match data[r][c]:
            case "|":
                yield r - 1, c
                yield r + 1, c
            case "-":
                yield r, c - 1
                yield r, c + 1
            case "L":
                yield r - 1, c
                yield r, c + 1
            case "J":
                yield r - 1, c
                yield r, c - 1
            case "7":
                yield r + 1, c
                yield r, c - 1
            case "F":
                yield r + 1, c
                yield r, c + 1
            case "S":
                yield r - 1, c
                yield r, c - 1
                yield r + 1, c
                yield r, c + 1
