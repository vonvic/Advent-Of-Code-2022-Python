"""Advent of Code Problem 08 Solution."""

from collections import namedtuple

Tree = namedtuple("Tuple", ["height", "left", "right", "top", "bottom"])


def get_matrix() -> list[list[int]]:
    mat: list[list[int]] = []
    
    with open("08/input.txt", "r") as f:
        for line in f:
            
            mat.append([int(val) for val in list(line.strip())])
    
    return mat

def get_matrix_v2() -> list[list[Tree]]:
    mat: list[list[int]] = []
    
    with open("08/input.txt", "r") as f:
        for line in f:
            for val in list(line.strip()):
                mat.append(Tree(int(val), 0, 0, 0, 0))
    
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


def get_scenic_score(mat: list[list[Tree]], loc: tuple[int, int]) -> int:
    left_count = 0
    right_count = 0
    top_count = 0
    bottom_count = 0
    
    n = len(mat)
    m = len(mat[0])
    
    i, j = loc
    height = mat[i][j]
    
    # left
    if j > 0:
        for x in range(j-1, -1, -1):
            cur_height = mat[i][x]
            if height > cur_height:
                left_count += 1
            elif height == cur_height:
                left_count += 1
                break
            else:
                break
        
    # right
    if j < m-1:
        for x in range(j+1, m):
            cur_height = mat[i][x]
            if height > cur_height:
                right_count += 1
            elif height == cur_height:
                right_count += 1
                break
            else:
                break
    
    # top
    if i > 0:
        for x in range(i-1, -1, -1):
            cur_height = mat[x][j]
            if height > cur_height:
                top_count += 1
            elif height == cur_height:
                top_count += 1
                break
            else:
                break
        
    # bottom
    if i < n-1:
        for x in range(i+1, n):
            cur_height = mat[x][j]
            if height > cur_height:
                bottom_count += 1
            elif height == cur_height:
                bottom_count += 1
                break
            else:
                break
    
    scenic_score = left_count * right_count * top_count * bottom_count
    # print(scenic_score)
    return scenic_score


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
    height_map = get_matrix()
    n = len(height_map)
    m = len(height_map[0])
    
    max_scenic_score = -1
    for i in range(n):
        for j in range(m):
            scenic_score = get_scenic_score(height_map, (i, j))
            max_scenic_score = max(max_scenic_score, scenic_score)
    return max_scenic_score