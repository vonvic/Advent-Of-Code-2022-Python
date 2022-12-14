"""Advent of Code Problem 06 Solution."""

def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    idx = 0
    with open("06/input.txt", "r") as f:
        seq = []
        while True:
            c = f.read(1)
            if not c:
                break
            
            seq.append(c)
            idx += 1
            if len(seq) < 4:
                continue
            else:
                if len(set(seq)) == 4:
                    break
                else:
                    seq.pop(0)
                
    return idx


def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    None
