from os import stat
from sys import flags


class Solution:
    def __init__(self, str_input):
        self.str_input = str_input

    def part1(self):
        """
        checks condn that at least three voiewls present
        """
        status = False
        count = 0
        for i in self.str_input:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                count += 1
        if count >= 3:
            status = True
        return status

    def part2(self):
        """
        contains one letter that apperas twice in a row
        xx ,dd,aabbccdd etc.
        """
        status = False
        count = 0
        for i in range(len(self.str_input) - 1):
            if self.str_input[i] == self.str_input[i + 1]:
                count += 1

        if count >= 1:
            status = True
        return status

    def part3(self):
        """
        does not conatins the strings ab ,cd ,pq or xy even if they are part of one of the
        other requirements
        """
        status = True
        for i in range(len(self.str_input) - 1):
            if self.str_input[i] == "a" and self.str_input[i + 1] == "b":
                status = False
                break
            elif self.str_input[i] == "c" and self.str_input[i + 1] == "d":
                status = False
                break
            elif self.str_input[i] == "p" and self.str_input[i + 1] == "q":
                status = False
                break
            elif self.str_input[i] == "x" and self.str_input[i + 1] == "y":
                status = False
                break

        return status


def main():
    input_stream = []
    with open("input.txt", "r") as f:
        inp = f.readlines()
        input_stream = [i.strip() for i in inp]
    count = 0
    for i in input_stream:
        p = Solution(i)
        if p.part1() and p.part2() and p.part3():
            count += 1

    print(count)


if __name__ == "__main__":
    main()
