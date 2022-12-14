"""Advent of Code Problem 07 Solution."""
from __future__ import annotations
from abc import ABC, abstractmethod
from functools import reduce

class File(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        
        
    @property
    def name(self):
        return self._name


    @property
    @abstractmethod
    def size(self):
        pass
    
    
class RegularFile(File):
    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self._size = size
    
    
    @property
    def size(self):
        return self._size
    
    def __str__(self):
        s = (
            "type: regular file",
            f"name: {self.name}",
            f"size: {self.size}"
        )
        return '\n'.join(s)


class Directory(File):
    def __init__(self, name: str, parent: Directory = None) -> None:
        super().__init__(name)
        self._contents: list[File] = []
        self._parent: Directory = parent


    @property
    def size(self):
        return reduce(lambda a, f: a+f.size, self._contents, 0)


    @property
    def contents(self):
        return self._contents


    @property
    def parent(self):
        return self._parent


    def add(self, file: File) -> None:
        self._contents.append(file)
        
        
    def does_file_exist(self, name: str) -> bool:
        return any(file.name == name for file in self._contents)
    

def tokenize(line: str) -> list[str]:
    return line.split()


def is_command(token: str) -> bool:
    return token == '$'


def get_root_from_dir(dir: Directory) -> Directory:
    while(dir.name != "/"):
        dir = dir.parent
    return dir


def sum_of_dir_at_most_size(dir: Directory, max_size: int) -> int:
    size_sum = dir.size if dir.size < max_size else 0
    for file in dir.contents:
        if not isinstance(file, Directory):
            continue
        
        size_sum += sum_of_dir_at_most_size(file, max_size)
    return size_sum


def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    curr_dir: Directory = Directory('/')
    with open("07/input.txt", "r") as f:
        for line in (l.strip() for l in f):
            tokens = tokenize(line)
            
            if is_command(tokens[0]):
                command = tokens[1]
                if command == "cd":
                    dest = tokens[2]
                    
                    if dest == ".." and curr_dir.parent != None:
                        curr_dir = curr_dir.parent
                        continue
                    
                    for file in curr_dir.contents:
                        if not isinstance(file, Directory):
                            continue
                        
                        if file.name == dest:
                            curr_dir = file
                            break
                elif command == "ls":
                    continue
                else:
                    raise Exception()
            else:
                filename = tokens[1]
                if not curr_dir.does_file_exist(filename):
                    if tokens[0] == "dir":
                        new_dir = Directory(filename, curr_dir)
                        curr_dir.add(new_dir)
                    else:
                        size = int(tokens[0])
                        new_reg_file = RegularFile(filename, size)
                        curr_dir.add(new_reg_file)
    root = get_root_from_dir(curr_dir)
    return sum_of_dir_at_most_size(root, 100000)


def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    None
