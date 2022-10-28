import re
from os import path
from tkinter import Tk, Canvas
from typing import Union, Tuple, List

from src import utils, config

with open(path.abspath(f'{utils.ROOT_DIR}/.env'), 'r') as env:
    play_music = env.readline().strip().split('=')[1]

if play_music == 'True':
    from vlc import MediaPlayer
    background_music = MediaPlayer(path.abspath('ressources/background-music.wav'))
else:
    class FakeMedia:
        def __init__(self):
            ...

        def play(self):
            return

        def stop(self):
            return

        def audio_set_volume(self, *args):
            return
    background_music = FakeMedia()

Matrix = List[List[int]]

SETTINGS = config.Settings().save(log=False)

PLAYERS = []

CURRENT_TURN = 0

TOKENS_NUMBER = 0

IS_PLAYING = False

FILLED_BOXES = {}

MOVES = []

BOXES_MATRIX = []

EMPTY = 2

ICON = path.abspath('ressources/window-icon.ico')

SOUNDS = {
    'token': path.abspath('ressources/token-sound.mp3'),
    'win': path.abspath('ressources/win-sound.mp3'),
    'loose': path.abspath('ressources/loose-sound.mp3'),
    'draw': path.abspath('ressources/draw-sound.mp3'),
    'background': background_music,
}

MODE = {
    'player_1': 'Player 1',
    'player_2': 'AI',
    'human_opponent_name': 'Player 2',
    'player_color_id': 0
}

WIN_PATTERNS = ['0000', '1111']


def init(window: Tk = None) -> None:
    from src.models.window import Window
    from src.models.player import HumanPlayer, AIPlayer
    from src.models.ai import RandomAI

    global CURRENT_TURN, TOKENS_NUMBER, IS_PLAYING, FILLED_BOXES, BOXES_MATRIX, PLAYERS

    CURRENT_TURN = 0
    TOKENS_NUMBER = 0
    IS_PLAYING = True
    FILLED_BOXES = {}
    BOXES_MATRIX = [
        [EMPTY for _ in range(SETTINGS.board_columns_number)]
        for _ in range(SETTINGS.board_rows_number)
    ]
    
    if window is not None:
        window.destroy()

    window = Window()

    player_1 = HumanPlayer(player_name=MODE.get('player_1', 'Player 1'),
                           color=SETTINGS.token_colors[MODE.get('player_color_id', 0)],
                           window=window)

    if MODE.get('player_2') == 'human':
        player_2 = HumanPlayer(player_name=MODE.get('human_opponent_name', 'Player 2'),
                               color=SETTINGS.token_colors[not MODE.get('player_color_id', 0)],
                               window=window)
    else:
        player_2 = AIPlayer(ai=RandomAI(),
                            color=SETTINGS.token_colors[not MODE.get('player_color_id', 0)],
                            window=window)

    PLAYERS = [player_1, player_2]

    window.run()


def get_color_from_identifier(widget_id: int, cnv: Canvas, normalize=False) -> int:
    if widget_id == EMPTY:
        return EMPTY if not normalize else -1
    else:
        return SETTINGS.token_colors.index(cnv.itemcget(widget_id, 'fill'))


def save_game_state() -> None:
    players = ['A', 'B']
    with open('games.csv', 'a') as file:
        moves = MOVES + [-1 for _ in range(42 - len(MOVES))]
        line = ','.join(map(str, moves))
        line += ',' + players[CURRENT_TURN] + '\n'
        file.write(line)


def find_four_in(matrix: Matrix, cnv: Canvas) -> Union[Tuple[int, List[int]], None]:
    for seq in matrix:
        categorized_seq = map(lambda identifier: str(get_color_from_identifier(identifier, cnv)), seq)
        joined_seq = ''.join(categorized_seq)

        for pattern in WIN_PATTERNS:
            result = re.findall(pattern, joined_seq)
            if result:
                win_index = joined_seq.index(result[0])
                return int(result[0][0]), seq[win_index:win_index+4]


def min_four_diags(matrix: Matrix) -> Matrix:
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


def find_four(canvas: Canvas) -> Union[Tuple[int, str], None]:
    reduced_matrix = list(filter(lambda r: any(map(lambda x: x != EMPTY, r)), BOXES_MATRIX))

    found = find_four_in(reduced_matrix, canvas)

    if found is None and len(reduced_matrix) >= 4:
        found = find_four_in(utils.transpose(reduced_matrix), canvas)

        if found is None:
            found = find_four_in(min_four_diags(reduced_matrix), canvas)

    return found
