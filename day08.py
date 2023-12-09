import math
import re

import base


class Solution(base.Solution):
    NODE_RE = re.compile(r"(\w+) = \((\w+), (\w+)\)")

    def load_data(self, input):
        chunks = input.split("\n\n")
        moves = [{"L": 0, "R": 1}[c] for c in chunks[0]]
        graph = {
            match.group(1): match.group(2, 3)
            for line in chunks[1].splitlines()
            if (match := self.NODE_RE.match(line))
        }
        return moves, graph

    def part1(self, data):
        return self.get_sequence_len(data, "AAA")

    def part2(self, data):
        _, graph = data
        return math.lcm(
            *(
                self.get_sequence_len(data, node)
                for node in graph
                if node.endswith("A")
            ),
        )

    def get_sequence_len(self, data, start):
        sequence = self.get_sequence(data, start)
        for count, node in enumerate(sequence, start=1):
            if node.endswith("Z"):
                return count

    def get_sequence(self, data, start):
        moves, graph = data
        node = start
        move_count = 0
        while True:
            next_nodes = graph[node]
            next_move = moves[move_count % len(moves)]
            node = next_nodes[next_move]
            move_count += 1
            yield node
