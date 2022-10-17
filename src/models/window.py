import tkinter as tk
from tkinter import messagebox

from src import game, config
from src.upload import upload_file
from src.logger import logger
from src.models.board import Board
from src.models.header import Header
from src.models.token import Token


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.settings = game.SETTINGS
        self.geometry_scale = self.settings.window_geometry_scale
        self.is_landscape = self.winfo_screenwidth() > self.winfo_screenheight()
        self.label_player_height = int(self.height * config.TITLE_HEIGHT_SCALE_REL_TO_HEIGHT)
        self.label_player_pad_x = int(self.width * 0.05)
        self.normal_font = ('TkDefaultFont', int(self.height * 0.025), 'bold')
        self.default_bg_color = self.cget('bg')
        self.rel_width = 1 - config.BOARD_SIZE_SCALE + 2 * config.BOARD_POS_X_SCALE_REL_TO_WIDTH

        self.title(self.settings.window_title)
        self.configure(background=self.settings.window_color)
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.on_exit)
        self.bind('<Escape>', self.on_exit)

        header = Header(self)
        header.set()

        self.board = Board(self)

        self.frame = tk.Frame(self, background=self.settings.window_color)
        self.frame.place(relx=(config.BOARD_SIZE_SCALE - 3 * config.BOARD_POS_X_SCALE_REL_TO_WIDTH),
                         rely=config.BOARD_POS_Y_SCALE_REL_TO_HEIGHT,
                         relwidth=self.rel_width,
                         height=self.board.height)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)

        self.label_player_1 = tk.Canvas(self.frame, height=self.label_player_height)
        self.label_player_1.grid(row=0, column=0, columnspan=2, sticky='ew')

        versus = tk.Label(self.frame,
                          text='VS',
                          font=(self.settings.font_family, 2 * self.normal_font[1], 'bold'),
                          background=self.settings.window_color)
        versus.grid(row=1, column=0, columnspan=2, sticky='ew')

        self.label_player_2 = tk.Canvas(self.frame, height=self.label_player_height)
        self.label_player_2.grid(row=2, column=0, columnspan=2, sticky='ew')

        self.start_button = tk.Button(self,
                                      text='START',
                                      font=self.normal_font,
                                      background='green',
                                      foreground='white',
                                      command=self.start)
        self.start_button.grid(in_=self.frame,
                               row=3, column=0,
                               columnspan=2,
                               ipadx=int(self.width * 0.025))

        self.retry_button = tk.Button(self,
                                      text='RETRY',
                                      font=self.normal_font,
                                      background='green',
                                      foreground='white',
                                      command=self.retry)
        self.retry_button.grid(in_=self.frame,
                               row=3, column=0,
                               columnspan=2,
                               ipadx=int(self.width * 0.025))
        self.retry_button.lower()

        self.exit_button = tk.Button(self,
                                     text='Exit',
                                     font=('TkDefaultFont', int(self.height * 0.0125), 'bold'),
                                     background='red',
                                     foreground='white',
                                     command=self.on_exit)
        self.exit_button.grid(in_=self.frame,
                              row=4, column=0,
                              columnspan=2,
                              ipadx=int(self.width * 0.025))
        self.exit_button.lower()

        logger.debug("Window initialised")
        logger.info(f'Window size: {self.width}x{self.height}')

    @property
    def width(self) -> int:
        return int(self.geometry_scale * self.winfo_screenwidth())

    @property
    def height(self) -> int:
        return int(self.geometry_scale * self.winfo_screenheight())

    def run(self) -> None:
        self.label_player_1.create_text(self.label_player_pad_x,
                                        self.label_player_height // 2,
                                        anchor='w',
                                        text=game.PLAYERS[0].name,
                                        font=self.normal_font)
        info_token = Token(self.label_player_1, game.PLAYERS[0])
        info_token.draw((int(self.width * self.rel_width) - self.label_player_pad_x, self.label_player_height // 2),
                        self.label_player_height // 3)

        self.label_player_2.create_text(self.label_player_pad_x,
                                        self.label_player_height // 2,
                                        anchor='w',
                                        text=game.PLAYERS[1].name,
                                        font=self.normal_font)
        info_token = Token(self.label_player_2, game.PLAYERS[1])

        info_token.draw((int(self.width * self.rel_width) - self.label_player_pad_x, self.label_player_height // 2),
                        self.label_player_height // 3)

        logger.info("Running...")

        self.mainloop()

    def start(self):
        self.start_button.lower()
        self.retry_button.lift(self.frame)
        self.exit_button.lift(self.frame)
        self.board.turn_highlight()
        self.board.bind('<Button-1>', self.board.at_human_player_click)

    def retry(self):
        game.init(self)

    def on_exit(self, event=None) -> None:
        if messagebox.askyesno(title="Exit game", message="Are you sure you want to exit ?"):
            logger.info("Exit App")
            try:
                upload_file('logs')
                if len(game.MOVES) >= 0:
                    upload_file('games')
                logger.info(f'Stats successfully uploaded')
            except Exception as error:
                logger.warning(f'Something went wrong while uploading stats: {error}')
            finally:
                self.destroy()
