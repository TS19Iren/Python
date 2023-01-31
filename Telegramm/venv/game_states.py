import enum

class Game_state(enum.Enum):
    START = 1
    INIT_GAME = 2
    GAME_IN_PROGRESS = 3
    END_GAME = 4