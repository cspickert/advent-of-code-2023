import base
import regex as re

class Solution(base.Solution):
    def load_data(self, input_str):
        return input_str.splitlines()

    def part1(self, data):
        return sum(self.calibration_values(data))

    def part2(self, data):
        return sum(self.calibration_values(data, replace_words=True))

    def calibration_values(self, data, replace_words=False):
        line_digits = [self.calibration_values_line(line, replace_words) for line in data]
        return [int(l[0] + l[-1]) for l in line_digits]

    def calibration_values_line(self, line, replace_words):
        replacements = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "ten": "10",
        }
        if replace_words:
            values_re = re.compile(r"one|two|three|four|five|six|seven|eight|nine|ten|\d")
        else:
            values_re = re.compile(r"\d")
        values = values_re.findall(line, overlapped=True)
        return [replacements[v] if v in replacements else v for v in values]
