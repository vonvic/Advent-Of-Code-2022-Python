"""Advent of Code Problem 03 Solution."""

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    misplaced_items: list[str] = []
    with open("03/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            m = len(line) // 2
            first, second = set(line[:m]), set(line[m:])
            misplaced = (first & second).pop()
            misplaced_items.append(misplaced)
    priorities = [letters.index(letter) + 1 for letter in misplaced_items]
    return sum(priorities)
            

def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    rugsacks: set[str] = set()
    badges: list[str] = []
    with open("03/input.txt", "r") as f:
        for line in f:
            rugsack = line.strip()
            rugsacks.add(rugsack)
            
            if len(rugsacks) < 3:
                continue

            first = set(rugsacks.pop())
            second = set(rugsacks.pop())
            third = set(rugsacks.pop())
            
            common = (first & second & third).pop()
            badges.append(common)
            
            rugsacks.clear()
    priorities = [letters.index(badge) + 1 for badge in badges]
    return sum(priorities)