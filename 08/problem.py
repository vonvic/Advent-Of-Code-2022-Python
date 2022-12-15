"""Advent of Code Problem 08 Solution."""

def get_matrix() -> list[list[int]]:
    mat: list[list[int]] = []
    
    with open("08/input.txt", "r") as f:
        for line in f:
            
            mat.append([int(val) for val in list(line.strip())])
    
    return mat


def find_all_visible_from_left(mat: list[list[int]]) -> set[tuple[int, int]]:
    visible: set[tuple[int, int]] = set()
    
    n = len(mat)
    m = len(mat[0])
    
    for i in range(n):
        cur_max = -1
        for j in range(m):
            cur_val = mat[i][j]
            if cur_val > cur_max:
                cur_max = cur_val
                visible.add((i, j))
    
    return visible

def find_all_visible_from_right(mat: list[list[int]]) -> set[tuple[int, int]]:
    visible: set[tuple[int, int]] = set()
    
    n = len(mat)
    m = len(mat[0])
    
    for i in range(n):
        cur_max = -1
        for j in range(m-1,-1, -1):
            cur_val = mat[i][j]
            if cur_val > cur_max:
                cur_max = cur_val
                visible.add((i, j))
    
    return visible

def find_all_visible_from_top(mat: list[list[int]]) -> set[tuple[int, int]]:
    visible: set[tuple[int, int]] = set()
    
    n = len(mat)
    m = len(mat[0])
    
    for i in range(m):
        cur_max = -1
        for j in range(n):
            cur_val = mat[j][i]
            if cur_val > cur_max:
                cur_max = cur_val
                visible.add((j, i))
    
    return visible

def find_all_visible_from_bottom(mat: list[list[int]]) -> set[tuple[int, int]]:
    visible: set[tuple[int, int]] = set()
    
    n = len(mat)
    m = len(mat[0])
    
    for i in range(m):
        cur_max = -1
        for j in range(n-1, -1, -1):
            cur_val = mat[j][i]
            if cur_val > cur_max:
                cur_max = cur_val
                visible.add((j, i))
    
    return visible

def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    height_map = get_matrix()
    left = find_all_visible_from_left(height_map)
    top = find_all_visible_from_top(height_map)
    right = find_all_visible_from_right(height_map)
    bottom = find_all_visible_from_bottom(height_map)
    
    visible = left | top | right | bottom
    
    return len(visible)
            

def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    None
