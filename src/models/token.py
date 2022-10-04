from typing import Tuple


class Token:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def draw(self, center: Tuple[int, int], radius: int) -> int:
        widget_id = self.board.create_oval(center[0] - radius,
                                           center[1] - radius,
                                           center[0] + radius,
                                           center[1] + radius,
                                           fill=self.player.color)
        return widget_id
