import tkinter as tk
from typing import Tuple

from src.logger import logger
from src.models.token import Token


def middle(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> Tuple[int, int]:
    return (point_2[0] + point_1[0]) // 2, (point_2[1] + point_1[1]) // 2


class Board(tk.Canvas):
    BOX_INNER_SCALE = 0.8
    FILLED_BOXES = {}

    def __init__(self, window, settings):
        self.window = window
        self.color = settings.board_color
        self.settings = settings
        self.border_thickness = settings.board_border_thickness
        self.columns_number = settings.board_columns_number
        self.rows_number = settings.board_rows_number

        size = self.size
        self.width = size[0]
        self.height = size[1]

        self.box_size = self.width // self.columns_number
        self.token_radius = (self.box_size * self.BOX_INNER_SCALE) // 2

        super().__init__(window,
                         width=self.width,
                         height=self.height,
                         background=self.color,
                         highlightthickness=self.border_thickness,
                         highlightbackground='black',
                         relief='sunken')

        self.create_grid()

        self.bind('<Button-1>', self.insert_token)

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

    def box_vertices(self, index_x: int, index_y: int) -> Tuple[int, int, int, int, Tuple[int, int]]:
        x_0 = self.border_thickness + (index_x * self.box_size)
        y_0 = self.border_thickness + (index_y * self.box_size)
        x_1 = self.border_thickness + ((index_x + 1) * self.box_size)
        y_1 = self.border_thickness + ((index_y + 1) * self.box_size)
        center = middle((x_0, y_0), (x_1, y_1))
        return x_0, y_0, x_1, y_1, center

    def create_grid(self) -> None:
        for x in range(self.columns_number):
            for y in range(self.rows_number):
                top_left_x, top_left_y, bottom_right_x, bottom_right_y, center = self.box_vertices(x, y)

                self.create_rectangle(top_left_x,
                                      top_left_y,
                                      bottom_right_x,
                                      bottom_right_y,
                                      width=self.border_thickness // 2,
                                      fill=self.color)

                self.create_oval(center[0] - self.token_radius,
                                 center[1] - self.token_radius,
                                 center[0] + self.token_radius,
                                 center[1] + self.token_radius,
                                 fill='white')

        logger.info("Grid created")

    def insert_token(self, event):
        box_index_x = event.x // self.box_size

        if box_index_x not in self.FILLED_BOXES:
            self.FILLED_BOXES[box_index_x] = [self.rows_number]

        last_box_y = self.FILLED_BOXES[box_index_x][-1]

        if last_box_y == 0:
            logger.debug("No token inserted")
        else:
            box_index_y = last_box_y - 1

            _, _, _, _, center = self.box_vertices(box_index_x, box_index_y)

            token = Token(self)
            token.draw(center, self.token_radius)

            self.FILLED_BOXES[box_index_x].append(box_index_y)

            logger.debug(f'Token inserted at column {box_index_x + 1} line {last_box_y}')
