"""Advent of Code Problem 01 Solution."""


def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    with open("01/input.txt", "r") as f:
        max_cal = 0
        for calories in f.read().split('\n\n'):
            cur_sum = sum((int(x) for x in calories.split()))
            max_cal = max(max_cal, cur_sum)
    return max_cal


def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    None

