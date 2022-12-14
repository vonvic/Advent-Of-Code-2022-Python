"""Advent of Code Problem 05 Solution."""


def init_stacks(inp: list[str]) -> list[list[str]]:
    """Initialize stack from text input."""
    last_idx = len(inp)-1
    count = int(inp[last_idx].split()[-1])
    
    stacks = [[] for _ in range(count)]
    
    OFFSET_INIT = 1
    OFFSET_SPACE = 4
    EMPTY = " "
    for row_idx in range(last_idx):
        for stack_idx in range(count):
            item_idx = OFFSET_INIT + OFFSET_SPACE * stack_idx
            item = inp[row_idx][item_idx]
            if item == EMPTY:
                continue
            
            stacks[stack_idx].append(item)
                
    print(stacks)
    return


def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    with open("05/input.txt", "r") as f:
        lines = f.readlines()
        
    end_of_init_idx = lines.index('\n')
    
    init_map = lines[:end_of_init_idx]
    move_list = lines[end_of_init_idx+1:]
    stacks = init_stacks(init_map)


def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    None
