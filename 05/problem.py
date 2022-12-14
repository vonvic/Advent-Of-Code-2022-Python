"""Advent of Code Problem 05 Solution."""

from collections import namedtuple

Move = namedtuple("Move", ["count", "src", "dest"])


def init_stacks(inp: list[str]) -> list[list[str]]:
    """Initialize stack from text input."""
    last_idx = len(inp)-1
    count = int(inp[last_idx].split()[-1])
    
    stacks = [[] for _ in range(count)]
    
    OFFSET_INIT = 1
    OFFSET_SPACE = 4
    EMPTY = " "
    for row_idx in range(last_idx-1, -1, -1):
        for stack_idx in range(count):
            item_idx = OFFSET_INIT + OFFSET_SPACE * stack_idx
            item = inp[row_idx][item_idx]
            if item == EMPTY:
                continue
            
            stacks[stack_idx].append(item)

    return stacks

def parse_move(move_txt: str) -> Move:
    """Parse the `move_txt` into a Move tuple."""
    return Move(*[int(n) for n in move_txt.split() if n.isdigit()])
    

def perform_move(stacks: list[list[str]], move: Move) -> None:
    """Pop and push from dest and src by count times specified in `move`."""
    for _ in range(move.count):
        dest, src = move.dest-1, move.src-1
        stacks[dest].append(stacks[src].pop())
        

def get_top_of_stacks(stacks: list[list[str]]) -> str:
    """Return a string of all the top of the stacks."""
    top = ""
    
    for stack in stacks:
        if stack:
            top += stack[-1]
    
    return top

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
    
    for move in (parse_move(m) for m in move_list):
        perform_move(stacks, move)

    return get_top_of_stacks(stacks)

def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    None
