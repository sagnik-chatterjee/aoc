from os import stat
from sys import flags
import re


class Solution:
    def __init__(self, str_input):
        self.str_input = str_input

    def part1(self):
        """
        contains a piar of any 2 letters that appeas at least twice in the string without overlapping
        like xyxy ao aabdefaa(aa)
        """
        char_list = []
        status = False
        count = 0
        for i in range(len(self.str_input) - 1):
            for j in range(len(self.str_input) - 1):
                if (self.str_input[i], self.str_input[i + 1]) == (
                    self.str_input[j],
                    self.str_input[j + 1],
                ):
                    if i != j:
                        count += 1
        if count > 0:
            status = True
        return status

    def part2(self):
        status = False
        count = 0
        for i in range(len(self.str_input) - 2):
            if self.str_input[i] == self.str_input[i + 2]:
                count += 1
        if count > 0:
            status = True

        return status


def main():
    input_stream = []
    with open("input.txt", "r") as f:
        inp = f.readlines()
        input_stream = [i.strip() for i in inp]
    count = 0
    for i in input_stream:
        p = Solution(i)
        if p.part1() and p.part2():
            count += 1
    print(count)


if __name__ == "__main__":
    main()
