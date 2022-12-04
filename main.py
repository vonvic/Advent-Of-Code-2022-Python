"""Driver program to run and display problems based on user selection.

The program dynamically loads the module from the problem folders after a user
enters a valid problem. The module must have public functions 'part_one_answer'
and 'part_two_answer'. Those functions will return an answer of any type, but
must be printable.
"""
import importlib
from typing import Any, NewType, Tuple

Answer = NewType("Answer", Any)


def get_problem_number() -> int:
    """Receives and parses a problem number from user input."""
    error_msg = "Invalid. Please enter a number in range of 1 through 25"

    problem: int
    while True:
        choice = input("Enter problem number [1-25] to run: ")
        if choice.isnumeric():
            problem = int(choice)
            if 1 <= problem <= 25:
                break
            else:
                print(error_msg)
        else:
            print(error_msg)
    return problem


def __run_problem(problem: int) -> Tuple[Answer, Answer]:
    """Import the problem module and returns its part one and two answers."""
    module_name = f"0{problem}" if 1 <= problem <= 9 else str(problem)
    module_name += ".problem"
    module = importlib.import_module(module_name)

    part_one: Answer
    part_two: Answer
    try:
        part_one = module.part_one_answer()
        part_two = module.part_two_answer()
    except AttributeError:
        raise AttributeError(
            "Error. Loaded problem module must have a part_one_answer and"
            "part_two_answer functions."
        )
    return part_one, part_two


def __display_answer(answers: Tuple[Answer, Answer]):
    """Display the answers from `answers`."""
    for i, v in enumerate(["one", "two"]):
        print(f"Part {v} answer:\n", answers[i], sep="")


def main():
    """Run and display answer from problem specified by user input."""
    problem: int = get_problem_number()
    answers: Tuple[Answer, Answer] = __run_problem(problem)
    __display_answer(answers)


if __name__ == "__main__":
    main()