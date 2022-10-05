import tkinter as tk
from tkinter import ttk

from src.models.header import Header
from src.logger import logger
from src import game, config


class GameModePopUp(tk.Tk):
    def __init__(self, settings):
        super().__init__()

        self.settings = settings
        self.geometry_scale = settings.popup_geometry_scale

        self.title("Game mode")
        self.configure(background=settings.window_color)
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.on_exit)
        self.bind('<Escape>', self.on_exit)
        self.bind('<Return>', self.save_data)

        header = Header(self)
        header.set()

        save_button = ttk.Button(self, text="Save", command=self.save_data)
        save_button.place(y=int(self.height * config.BOARD_POS_Y_SCALE_REL_TO_HEIGHT))

        logger.debug("Game mode configuration popup initialised")
        logger.info(f'Popup window size: {self.width}x{self.height}')

    @property
    def width(self) -> int:
        return int(self.geometry_scale * self.winfo_screenwidth())

    @property
    def height(self) -> int:
        return int(self.geometry_scale * self.winfo_screenheight())

    def show(self) -> None:
        logger.info("Pending for game mode")
        self.mainloop()

    def save_data(self, event=None) -> None:
        logger.info(f'Game Mode: {None}')

    def on_exit(self, event=None) -> None:
        self.destroy()
