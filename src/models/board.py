import tkinter as tk
from typing import Tuple

from playsound import playsound

from src.logger import logger
from src.models.token import Token
from src.models.player import HumanPlayer, AIPlayer
from src import game, config, utils


class Board(tk.Canvas):
    BOX_INNER_SCALE = 0.8

    def __init__(self, window):
        self.window = window
        self.color = game.SETTINGS.board_color
        self.border_thickness = game.SETTINGS.board_border_thickness
        self.columns_number = game.SETTINGS.board_columns_number
        self.rows_number = game.SETTINGS.board_rows_number
        self.boxes = []

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
                         relief='raised')

        self.create_grid()

        if self.window.is_landscape:
            self.place(x=int(self.window.width * config.BOARD_POS_X_SCALE_REL_TO_WIDTH),
                       y=int(self.window.height * config.BOARD_POS_Y_SCALE_REL_TO_HEIGHT))
        else:
            ...

        logger.debug("Board initialized")
        logger.info(f'Board size: {self.width}x{self.height}')

    @property
    def size(self) -> Tuple[int, int]:
        if self.window.is_landscape:
            pre_height = int(self.window.height * config.BOARD_SIZE_SCALE)
            height = pre_height - (pre_height % self.rows_number)
            width = (height // self.rows_number) * self.columns_number
        else:
            pre_width = int(self.window.width * config.BOARD_SIZE_SCALE)
            width = pre_width - (pre_width % self.columns_number)
            height = (width // self.columns_number) * self.rows_number

        return width, height

    def box_vertices(self, index_x: int, index_y: int) -> Tuple[int, int, int, int, Tuple[int, int]]:
        x_0 = self.border_thickness + (index_x * self.box_size)
        y_0 = self.border_thickness + (index_y * self.box_size)
        x_1 = self.border_thickness + ((index_x + 1) * self.box_size)
        y_1 = self.border_thickness + ((index_y + 1) * self.box_size)
        center = utils.middle((x_0, y_0), (x_1, y_1))

        return x_0, y_0, x_1, y_1, center

    def create_grid(self) -> None:
        for x in range(self.columns_number):
            for y in range(self.rows_number):
                top_left_x, top_left_y, bottom_right_x, bottom_right_y, center = self.box_vertices(x, y)

                box = self.create_rectangle(top_left_x,
                                            top_left_y,
                                            bottom_right_x,
                                            bottom_right_y,
                                            width=self.border_thickness // 2,
                                            fill=self.color)

                self.boxes.append(box)

                self.create_oval(center[0] - self.token_radius,
                                 center[1] - self.token_radius,
                                 center[0] + self.token_radius,
                                 center[1] + self.token_radius,
                                 fill='white')

    def matching_box(self, token_id) -> int:
        for box in self.boxes:
            box_coords = self.coords(box)
            token_coords = self.coords(token_id)

            condition_1 = box_coords[0] < token_coords[0]
            condition_2 = box_coords[1] < token_coords[1]
            condition_3 = box_coords[2] > token_coords[2]
            condition_4 = box_coords[3] > token_coords[3]

            if condition_1 and condition_2 and condition_3 and condition_4:
                return box

    def at_human_player_click(self, event) -> None:
        if game.IS_PLAYING:
            col = event.x // self.box_size
            player = game.PLAYERS[game.CURRENT_TURN]

            if isinstance(player, HumanPlayer):
                insertion_ok = self.insert_token(player, col)
                if game.IS_PLAYING and game.TOKENS_NUMBER < self.rows_number * self.columns_number:
                    if insertion_ok:
                        self.switch_turn()
                        self.window.after(200, self.next_move)
                else:
                    self.end_game()

    def next_move(self):
        player = game.PLAYERS[game.CURRENT_TURN]
        if isinstance(player, AIPlayer):
            self.insert_token(player, player.move())
            if game.IS_PLAYING and game.TOKENS_NUMBER < self.rows_number * self.columns_number:
                self.switch_turn()
            else:
                self.end_game()

    def switch_turn(self):
        game.CURRENT_TURN = not game.CURRENT_TURN
        self.turn_highlight()

    def insert_token(self, player, box_index_x: int) -> bool:
        inserted = False

        if box_index_x not in game.FILLED_BOXES:
            game.FILLED_BOXES[box_index_x] = [self.rows_number]

        last_box_y = game.FILLED_BOXES[box_index_x][-1]

        if last_box_y == 0:
            logger.debug(f'{player.name} ({player.color}): No token inserted')
        else:
            box_index_y = last_box_y - 1

            _, _, _, _, center = self.box_vertices(box_index_x, box_index_y)

            token = Token(self, player)

            game.BOXES_MATRIX[box_index_y][box_index_x] = token.draw(center, self.token_radius)

            playsound(game.SOUNDS['token'])

            game.FILLED_BOXES[box_index_x].append(box_index_y)

            game.TOKENS_NUMBER += 1

            inserted = True

            logger.debug(f'{player.name} ({player.color}) move: '
                         f'column {box_index_x + 1} line {last_box_y}')

            if game.TOKENS_NUMBER >= 7:
                win_state = game.find_four(self)

                if win_state is not None:
                    game.IS_PLAYING = False
                    self.turn_highlight(ended=True)
                    for win_token in win_state[1]:
                        self.itemconfigure(self.matching_box(win_token), fill='green')

        return inserted

    def turn_highlight(self, ended=False):
        players = {
            0: self.window.label_player_1,
            1: self.window.label_player_2
        }
        players[not game.CURRENT_TURN].configure(background=self.window.default_bg_color)

        if not ended:
            players[game.CURRENT_TURN].configure(background='green')
        else:
            players[game.CURRENT_TURN].configure(background=self.window.default_bg_color)

    def end_game(self):
        logger.debug(f'{game.IS_PLAYING}, {game.TOKENS_NUMBER < self.rows_number * self.columns_number}')
