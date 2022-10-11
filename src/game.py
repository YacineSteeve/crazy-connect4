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


def four_in(seq: List[int]) -> Union[bool, Tuple[bool, str, str]]:
    joined_row = ''.join(map(str, seq))

    for pattern in WIN_PATTERNS:
        result = re.findall(pattern, joined_row)
        if result:
            position = joined_row.index(result[0])
            return True, result[0], joined_row

    return False


def min_four_diags(matrix: List[List[int]]) -> List[List[int]]:
    n, m = len(matrix), len(matrix[0])
    diags = []

    if m >= 4:
        for col in range(0, m - 3):
            diag = []
            row = 0
            while row < n and col < m:
                diag.append(matrix[row][col])
                row += 1
                col += 1
            diags.append(diag)

        for col in range(3, m):
            diag = []
            row = 0
            while row < n and col >= 0:
                diag.append(matrix[row][col])
                row += 1
                col -= 1
            diags.append(diag)

    if n >= 5:
        for row in range(1, n - 4):
            diag = []
            col = m - 1
            while row < n and col >= 0:
                diag.append(matrix[row][col])
                row += 1
                col -= 1
            diags.append(diag)

        for row in range(1, n - 4):
            diag = []
            col = 0
            while row < n and col < m:
                diag.append(matrix[row][col])
                row += 1
                col += 1
            diags.append(diag)

    return diags


def find_four() -> Union[bool, Tuple[bool, int]]:
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

        for diag in min_four_diags(reduced_matrix):
            res = four_in(diag)
            if res:
                logger.debug(f'Diag : {res}')
                break

    return False


def game_over():
    ...
