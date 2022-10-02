import tkinter as tk
from typing import Tuple

from src.logger import logger


def middle(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> Tuple[int, int]:
    return (point_2[0] + point_1[0]) // 2, (point_2[1] + point_1[1]) // 2


class Board(tk.Canvas):
    BOX_INNER_SCALE = 0.8

    def __init__(self, window, settings):
        self.window = window
        self.color = settings.board_color
        self.border_thickness = settings.board_border_thickness
        self.columns_number = settings.board_columns_number
        self.rows_number = settings.board_rows_number

        size = self.size
        self.width = size[0]
        self.height = size[1]

        self.box_size = self.width // self.columns_number

        super().__init__(window,
                         width=self.width,
                         height=self.height,
                         background=self.color,
                         highlightthickness=self.border_thickness,
                         highlightbackground='black',
                         relief='sunken')

        self.create_grid()

        if self.window.is_landscape:
            self.place(x=int(self.window.width * self.window.BOARD_POS_X_SCALE_REL_TO_WIDTH),
                       y=int(self.window.height * self.window.BOARD_POS_Y_SCALE_REL_TO_HEIGHT))
        else:
            ...

        logger.debug("Board initialized")

    @property
    def size(self) -> Tuple[int, int]:
        if self.window.is_landscape:
            pre_height = int(self.window.height * self.window.BOARD_SIZE_SCALE)
            height = pre_height - (pre_height % self.rows_number)
            width = (height // self.rows_number) * self.columns_number
        else:
            pre_width = int(self.window.width * self.window.BOARD_SIZE_SCALE)
            width = pre_width - (pre_width % self.columns_number)
            height = (width // self.columns_number) * self.rows_number

        logger.info(f'Board size: {width}x{height}')

        return width, height

    def create_grid(self) -> None:
        radius = (self.box_size * self.BOX_INNER_SCALE) // 2

        for x in range(self.columns_number):
            for y in range(self.rows_number):
                top_left_x = self.border_thickness + (x * self.box_size)
                top_left_y = self.border_thickness + (y * self.box_size)
                bottom_right_x = self.border_thickness + ((x + 1) * self.box_size)
                bottom_right_y = self.border_thickness + ((y + 1) * self.box_size)

                center = middle((top_left_x, top_left_y), (bottom_right_x, bottom_right_y))

                self.create_rectangle(top_left_x,
                                      top_left_y,
                                      bottom_right_x,
                                      bottom_right_y,
                                      width=self.border_thickness // 2,
                                      fill=self.color)

                self.create_oval(center[0] - radius,
                                 center[1] - radius,
                                 center[0] + radius,
                                 center[1] + radius,
                                 fill='white')

        logger.info("Grid created")
