import random
from random import randint
import game_config


def smart_bot_turn(total: int)->int:
    if total >= 29:
        if total - game_config.max_taken_sweets <= game_config.max_taken_sweets:
            taken_sweets = randint(1, total - game_config.max_taken_sweets - 1)
        else:
            taken_sweets = randint((total - 29) % 29, 28)
    elif total == game_config.max_taken_sweets:
        taken_sweets = game_config.max_taken_sweets
    else:
        taken_sweets = total
    return taken_sweets


def left_sweets(taken_sweets: int, total: int) -> int:
    total -= taken_sweets
    return total


def validate_answer(taken_sweets: str, max_taken_sweets: int):
    return taken_sweets.isdigit() and max_taken_sweets >= int(taken_sweets) > 0


def get_rnd_answer_when_not_valid():
    return game_config.list_angry_comments[random.randint(0,len(game_config.list_angry_comments)-1)]

def check_end_game(total: int):
    return total == 0

