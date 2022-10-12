import re
from typing import Union, Tuple, List

from src import utils

SETTINGS = None

PLAYERS = []

CURRENT_TURN = 0

TOKENS_NUMBER = 0

IS_PLAYING = False

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


def find_four_in(matrix: List[List[int]]) -> Union[Tuple[int, str], None]:
    for seq in matrix:
        joined_seq = ''.join(map(str, seq))

        for pattern in WIN_PATTERNS:
            result = re.findall(pattern, joined_seq)
            if result:
                return int(result[0][0]), joined_seq


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


def find_four() -> Union[Tuple[int, str], None]:
    reduced_matrix = list(filter(lambda r: any(map(lambda x: x != EMPTY, r)), BOXES_MATRIX))

    found = find_four_in(reduced_matrix)

    if found is None and len(reduced_matrix) >= 4:
        found = find_four_in(utils.transpose(reduced_matrix))

        if found is None:
            found = find_four_in(min_four_diags(reduced_matrix))

    return found
