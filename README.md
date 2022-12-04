# Advent-Of-Code-Python-Template
This is a template for Advent of Code with Python. Each folder corresponds to the day of the selected Advent of Code problem set. For each folder, it contains:
- `problem.py`: Your solution code. 
- `input.txt`: The input text.

## How To Run
In terminal, run
```bash
python3 main.py
```
You will then be prompted to choose the day problem to run. After selecting a problem it will load then run the `part_one_answer` and `part_two_answer` functions located in the corresponding `problem.py` of the selected problem.
```
Enter problem number [1-25] to run: 01
Part one answer:
None
Part two answer:
None
```

## How To Implement Your Solution
In the selected `problem.py`, your answer for part one should be returned by `part_one_answer`. The same goes for your part two answer. Your `problem.py` should not print directly, as printing is already handled by `main.py`.