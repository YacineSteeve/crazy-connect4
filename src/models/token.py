from typing import Tuple


class Token:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.outline_width = (self.board.border_thickness * 3) // 4

    def draw(self, center: Tuple[int, int], radius: int) -> int:
        widget_id = self.board.create_oval(center[0] - radius,
                                           center[1] - radius,
                                           center[0] + radius,
                                           center[1] + radius,
                                           fill=self.player.color,
                                           outline='black',
                                           width=self.outline_width)
        return widget_id
