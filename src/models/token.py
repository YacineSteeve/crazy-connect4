from typing import Tuple


class Token:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.player = player

        try:
            self.outline_width = (self.canvas.border_thickness * 3) // 4
        except AttributeError:
            from src import game
            self.outline_width = (game.SETTINGS.board_border_thickness * 3) // 4

    def draw(self, center: Tuple[int, int], radius: int) -> int:
        widget_id = self.canvas.create_oval(center[0] - radius,
                                            center[1] - radius,
                                            center[0] + radius,
                                            center[1] + radius,
                                            fill=self.player.color,
                                            outline='black',
                                            width=self.outline_width)
        return widget_id
