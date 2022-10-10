import re
from typing import Union, Tuple, List

from src.logger import logger
from src import utils

SETTINGS = None

PLAYERS = []

CURRENT_TURN = 0

TOKENS_NUMBER = 0

FILLED_BOXES = {}

BOXES_MATRIX = []

EMPTY = 2

MODE = {
    'player_1': 'Player 1',
    'player_2': 'AI',
    'human_opponent_name': 'Player 2',
    'player_color_id': 0
}

WIN_PATTERNS = ['0000', '1111']


def four_in(seq: List[int]) -> Union[bool, Tuple[bool, str, int, int]]:
    joined_row = ''.join(map(str, seq))

    for pattern in WIN_PATTERNS:
        result = re.findall(pattern, joined_row)
        if result:
            position = joined_row.index(result[0])
            return True, result[0], position, position + 3

    return False


def find_four(settings=None) -> Union[bool, Tuple[bool, int]]:
    settings = SETTINGS
    reduced_matrix = list(filter(lambda r: any(map(lambda x: x != EMPTY, r)), BOXES_MATRIX))

    for row in reduced_matrix:
        res = four_in(row)
        if res:
            logger.debug(f'Row : {res}')
            break

    if len(reduced_matrix) >= 4:
        for col in utils.transpose(reduced_matrix):
            res = four_in(col)
            if res:
                logger.debug(f'Col : {res}')
                break

    return False


def game_over():
    ...
