"""Advent of Code Problem 02 Solution."""

def _determine_winner(opp: str, you: str) -> int:
    """
    Determine the winner of rock-paper-scissors with number.
    
    The results are:
        win => 6
        draw => 3
        loss => 0
    """
    offset: int
    match you:
        case 'paper':
            offset = 0
        case 'rock':
            offset = 1
        case 'scissor':
            offset = 2
        case _:
            raise Exception()
    
    opp_init: int
    match opp:
        case 'rock':
            opp_init = 0
        case 'paper':
            opp_init = 1
        case 'scissor':
            opp_init = 2
        case _:
            raise Exception()
    
    opp_score = (opp_init + offset) % 3
    
    if opp_score < 1:
        return 6
    elif opp_score == 1:
        return 3
    else:
        return 0
    

def _play(opp: str, you: str) -> int:
    """Play the moves of `opp` and `you` and return score."""
    outcome_score: int
    match you:
        case 'rock':
            outcome_score = 1
        case 'paper':
            outcome_score = 2
        case 'scissor':
            outcome_score = 3

    outcome_score += _determine_winner(opp, you)
    return outcome_score


def get_player_move_from_letter(letter: str):
    """Return player move from letter."""
    match letter:
        case 'X':
            return 'rock'
        case 'Y':
            return 'paper'
        case 'Z':
            return 'scissor'


def get_opp_move_from_letter(letter: str):
    """Return opponent move from letter."""
    match letter:
        case 'A':
            return 'rock'
        case 'B':
            return 'paper'
        case 'C':
            return 'scissor'



def part_one_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    score = 0
    with open("02/input.txt", "r") as f:
        for line in f:
            opp, you = line.strip().split(' ')
            opp = get_opp_move_from_letter(opp)
            you = get_player_move_from_letter(you)
            score += _play(opp, you)
    return score


def part_two_answer() -> int:
    """
    Advent of Code Part One Answer.
    """
    None
