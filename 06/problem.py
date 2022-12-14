"""Advent of Code Problem 06 Solution."""

from io import TextIOWrapper


def end_idx_of_uniq_seq(f: TextIOWrapper, length: int) -> int:
    idx = 0
    seq = []
    while True:
        c = f.read(1)
        if not c:
            break
        
        seq.append(c)
        idx += 1
        if len(seq) < length:
            continue
        else:
            if len(set(seq)) == length:
                break
            else:
                seq.pop(0)
    return idx

def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    idx = 0
    with open("06/input.txt", "r") as f:
        idx = end_idx_of_uniq_seq(f, 4)
                
    return idx


def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    idx = 0
    with open("06/input.txt", "r") as f:
        idx = end_idx_of_uniq_seq(f, 14)
                
    return idx
