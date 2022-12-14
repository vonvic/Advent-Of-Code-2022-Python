"""Advent of Code Problem 04 Solution."""

def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    fully_overlap_count = 0
    with open("04/input.txt", "r") as f:
        for line in f:
            pair_assignments = line.strip()
            fst, snd = pair_assignments.split(',')
            fst_st, fst_end = fst.split('-')
            snd_st, snd_end = snd.split('-')
            fst_st = int(fst_st)
            fst_end = int(fst_end)
            snd_st = int(snd_st)
            snd_end = int(snd_end)
            
            if fst_st <= snd_st and snd_end <= fst_end:
                fully_overlap_count += 1
            elif snd_st <= fst_st and fst_end <= snd_end:
                fully_overlap_count += 1
            
    return fully_overlap_count


def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    overlap_count = 0
    with open("04/input.txt", "r") as f:
        for line in f:
            pair_assignments = line.strip()
            fst, snd = pair_assignments.split(',')
            fst_st, fst_end = fst.split('-')
            snd_st, snd_end = snd.split('-')
            fst_st = int(fst_st)
            fst_end = int(fst_end)
            snd_st = int(snd_st)
            snd_end = int(snd_end)
            
            if snd_st <= fst_st <= snd_end or\
                snd_st <= fst_end <= snd_end or\
                fst_st <= snd_st <= fst_end or\
                fst_st <= snd_end <= fst_end:
                overlap_count += 1
            
    return overlap_count