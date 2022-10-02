import tkinter as tk
from tkinter import font

from src.config import Settings
from src.logger import logger
from src.models.board import Board


class Window(tk.Tk):
    WINDOW_GEOMETRY_SCALE = 0.5

    TITLE_POS_Y_SCALE_REL_TO_HEIGHT = 0.05
    TITLE_HEIGHT_SCALE_REL_TO_HEIGHT = 2 * TITLE_POS_Y_SCALE_REL_TO_HEIGHT
    TITLE_WIDTH_SCALE_REL_TO_WIDTH = 0.45
    TITLE_POS_X_SCALE_REL_TO_WIDTH = (1 - TITLE_WIDTH_SCALE_REL_TO_WIDTH) / 2

    BOARD_POS_X_SCALE_REL_TO_WIDTH = 0.05
    BOARD_POS_Y_SCALE_REL_TO_HEIGHT = TITLE_HEIGHT_SCALE_REL_TO_HEIGHT + (2 * TITLE_POS_Y_SCALE_REL_TO_HEIGHT)
    BOARD_SIZE_SCALE = 1 - TITLE_HEIGHT_SCALE_REL_TO_HEIGHT - (3 * TITLE_POS_Y_SCALE_REL_TO_HEIGHT)

    def __init__(self, settings: Settings):
        super().__init__()
        self.is_landscape = self.winfo_screenwidth() > self.winfo_screenheight()

        self.title_widget(settings)

        self.board = Board(self, settings)

        self.title(settings.window_title)
        self.configure(background=settings.window_color)
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.on_exit)
        self.bind('<Escape>', self.on_exit)

        logger.debug("Window initialised")
        logger.info(f'Window size: {self.width}x{self.height}')

    @property
    def width(self) -> int:
        return int(self.WINDOW_GEOMETRY_SCALE * self.winfo_screenwidth())

    @property
    def height(self) -> int:
        return int(self.WINDOW_GEOMETRY_SCALE * self.winfo_screenheight())

    def run(self) -> None:
        logger.info("Running...")
        self.mainloop()

    def on_exit(self, *args, **kwargs) -> None:
        logger.debug("Exit App")
        self.destroy()

    def title_widget(self, settings: Settings) -> None:
        text_font = font.Font(family=settings.font_family,
                              size=int(self.height * 0.05),
                              weight='bold')
        text = tk.Label(self,
                        text=settings.window_title,
                        font=text_font,
                        justify='left',
                        anchor='center',
                        background=settings.window_color,
                        compound='center')

        text.place(x=int(self.width * self.TITLE_POS_X_SCALE_REL_TO_WIDTH),
                   y=int(self.height * self.TITLE_POS_Y_SCALE_REL_TO_HEIGHT),
                   width=int(self.width * self.TITLE_WIDTH_SCALE_REL_TO_WIDTH),
                   height=int(self.height * self.TITLE_HEIGHT_SCALE_REL_TO_HEIGHT),
                   bordermode='outside')
