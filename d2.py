from typing import List
from pathlib import Path


def part1(x: List[str]) -> int:
    n_valid = 0
    for line in x:
        min_, max_, character, pw = line.replace(":", " ").replace("-", " ").split()
        if int(min_) <= pw.count(character) <= int(max_):
            n_valid += 1
    return n_valid


def part2(x: List[str]) -> int:
    n_valid = 0
    for line in x:
        min_, max_, character, pw = line.replace(":", " ").replace("-", " ").split()
        try:
            if (pw[int(min_) - 1] == character) ^ (pw[int(max_) - 1] == character):
                n_valid += 1
        except IndexError:
            pass
    return n_valid


def solve_part1():
    with open(Path("inputs/d2p1.txt")) as f:
        inputs = f.readlines()
    return part1(inputs)


def solve_part2():
    with open(Path("inputs/d2p1.txt")) as f:
        inputs = f.readlines()
    return part2(inputs)


def test_part1():
    assert part1(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 2


def test_part2():
    assert part2(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 1


if __name__ == "__main__":
    print(solve_part1())
    print(solve_part2())
