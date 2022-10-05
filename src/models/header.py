import tkinter as tk
from tkinter import font

from src import config


class Header(tk.Label):
    def __init__(self, window):
        self.window = window

        text_font = font.Font(family=window.settings.font_family,
                              size=int(window.height * 0.05),
                              weight='bold')

        super().__init__(window,
                         text=window.settings.window_title,
                         font=text_font,
                         justify='left',
                         anchor='center',
                         background=window.settings.window_color,
                         compound='center')

    def set(self) -> None:
        self.place(x=int(self.window.width * config.TITLE_POS_X_SCALE_REL_TO_WIDTH),
                   y=int(self.window.height * config.TITLE_POS_Y_SCALE_REL_TO_HEIGHT),
                   width=int(self.window.width * config.TITLE_WIDTH_SCALE_REL_TO_WIDTH),
                   height=int(self.window.height * config.TITLE_HEIGHT_SCALE_REL_TO_HEIGHT),
                   bordermode='outside')
