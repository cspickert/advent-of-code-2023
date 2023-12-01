import importlib
import logging
from argparse import ArgumentParser
from pathlib import Path

logging.basicConfig()


class Runner:
    def __init__(self, day_module, input_path):
        self.solution = self.load_solution(day_module)
        self.input_path = input_path

    def load_solution(self, day_module):
        solution_module = importlib.import_module(day_module)
        solution_cls = getattr(solution_module, "Solution")
        return solution_cls()

    def load_input(self):
        with self.input_path.open() as input_file:
            return input_file.read()

    def run_method(self, method_name):
        input_str = self.load_input()
        solution_input = self.solution.load_data(input_str)
        solution_method = getattr(self.solution, method_name)
        return solution_method(solution_input)

    def run_part1(self):
        return self.run_method("part1")

    def run_part2(self):
        input_str = self.load_input()
        return self.run_method("part2")

    def run(self):
        if (part1_result := self.run_part1()) is not None:
            print(part1_result)
        if (part2_result := self.run_part2()) is not None:
            print(part2_result)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("day_module", help="The day module to run, e.g. day01")
    args = parser.parse_args()
    input_path = Path(__file__).parent / "input" / f"{args.day_module}.txt"
    runner = Runner(args.day_module, input_path)
    runner.run()
