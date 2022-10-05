import tkinter as tk

from src.logger import logger
from src.models.board import Board
from src.models.header import Header


class Window(tk.Tk):
    def __init__(self, settings):
        super().__init__()

        self.settings = settings
        self.geometry_scale = settings.window_geometry_scale
        self.is_landscape = self.winfo_screenwidth() > self.winfo_screenheight()

        self.title(settings.window_title)
        self.configure(background=settings.window_color)
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.on_exit)
        self.bind('<Escape>', self.on_exit)

        header = Header(self)
        header.set()

        self.board = Board(self)

        logger.debug("Window initialised")
        logger.info(f'Window size: {self.width}x{self.height}')

    @property
    def width(self) -> int:
        return int(self.geometry_scale * self.winfo_screenwidth())

    @property
    def height(self) -> int:
        return int(self.geometry_scale * self.winfo_screenheight())

    def run(self) -> None:
        logger.info("Running...")
        self.mainloop()

    def on_exit(self, event=None) -> None:
        logger.debug("Exit App")
        self.destroy()
