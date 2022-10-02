from typing import Tuple
from random import choice


class Token:
    def __init__(self, board, player=None):
        self.board = board
        self.player = player

    def draw(self, center: Tuple[int, int], radius: int):
        self.board.create_oval(center[0] - radius,
                               center[1] - radius,
                               center[0] + radius,
                               center[1] + radius,
                               fill=choice(self.board.settings.token_colors))
