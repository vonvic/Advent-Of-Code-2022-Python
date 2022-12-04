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
    with open("01/input.txt", "r") as f:
        top_three_cal = [0, 0, 0]
        for calories in f.read().split('\n\n'):
            cur_sum = sum((int(x) for x in calories.split()))
            
            third = min(top_three_cal)
            third_idx = top_three_cal.index(third)
            
            if cur_sum > third:
                top_three_cal[third_idx] = cur_sum
    return sum(top_three_cal)

