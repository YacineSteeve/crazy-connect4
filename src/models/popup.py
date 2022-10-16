import sys
import tkinter as tk
from tkinter import ttk, font

from src.models.header import Header
from src.logger import logger
from src import game, config


class GameModePopUp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.settings = game.SETTINGS
        self.geometry_scale = self.settings.popup_geometry_scale
        self.pad = int(self.height * config.TITLE_POS_Y_SCALE_REL_TO_HEIGHT)
        self.grid_pad_x = self.pad // 2
        self.player_name = tk.StringVar()
        self.opponent = tk.StringVar()
        self.opponent_name = tk.StringVar()
        self.player_color = tk.IntVar()

        self.title("Game mode")
        self.configure(background=self.settings.window_color)
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.on_exit)
        self.bind('<Escape>', self.on_exit)
        self.bind('<Return>', self.save_data)

        header = Header(self)
        header.set()

        self.frame = tk.Frame(self, background=self.settings.window_color)
        self.frame.place(relx=(1 - config.TITLE_WIDTH_SCALE_REL_TO_WIDTH) / 2,
                         rely=(2 * config.TITLE_HEIGHT_SCALE_REL_TO_HEIGHT),
                         relheight=(1 - 2.25 * config.TITLE_HEIGHT_SCALE_REL_TO_HEIGHT),
                         relwidth=config.TITLE_WIDTH_SCALE_REL_TO_WIDTH)
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        default_font_size = font.nametofont('TkDefaultFont').cget('size')

        question = tk.Label(self.frame,
                            text="Welcome!",
                            font=('TkDefaultFont', int(default_font_size * 1.2)),
                            background=self.settings.window_color)

        question.grid(row=0, column=0, columnspan=3, sticky='ew', pady=self.pad)

        ask_player_name = tk.Label(self.frame, text="Your name :", background=self.settings.window_color)
        ask_player_name.grid(row=1, column=0, sticky='w', padx=self.grid_pad_x, pady=self.grid_pad_x)

        player_name_entry = tk.Entry(self.frame, textvariable=self.player_name)
        player_name_entry.grid(row=1, column=1, sticky='e', pady=self.grid_pad_x)
        player_name_entry.focus_set()

        ask_opponent = tk.Label(self.frame, text="Play against :", background=self.settings.window_color)
        ask_opponent.grid(row=2, column=0, sticky='w', padx=self.grid_pad_x, pady=self.grid_pad_x)

        entry_width = player_name_entry.cget('width')

        choose_opponent = ttk.Combobox(self.frame,
                                       textvariable=self.opponent,
                                       width=entry_width-1,
                                       justify='center',
                                       state='readonly')
        choose_opponent['values'] = ('-Choose opponent-', 'Human', 'AI')
        choose_opponent.current(0)
        choose_opponent.bind('<<ComboboxSelected>>', self.on_opponent_choice)
        choose_opponent.grid(row=2, column=1, sticky='e', pady=self.grid_pad_x)

        self.human_opponent_name = tk.Label(self, text="Opponent's name :", background=self.settings.window_color)
        self.human_opponent_name.grid(in_=self.frame,
                                      row=3, column=0,
                                      sticky='e',
                                      ipadx=self.grid_pad_x // 2,
                                      pady=self.grid_pad_x)
        self.human_opponent_name.lower(self.frame)

        self.human_opponent_name_entry = tk.Entry(self, textvariable=self.opponent_name)
        self.human_opponent_name_entry.grid(in_=self.frame,
                                            row=3, column=1,
                                            sticky='e',
                                            pady=self.grid_pad_x)
        self.human_opponent_name_entry.lower(self.frame)

        ask_color = tk.Label(self.frame,
                             text="Choose your color\n(the other one will be for your opponent)",
                             background=self.settings.window_color)

        ask_color.grid(row=4, column=0, columnspan=3, sticky='ew', pady=self.grid_pad_x)

        color_1 = tk.Radiobutton(self.frame,
                                 variable=self.player_color,
                                 text=self.settings.token_colors[0].title(),
                                 value=0,
                                 background=self.settings.window_color,
                                 activebackground=self.settings.token_colors[0],
                                 highlightbackground=self.settings.window_color)
        color_1.select()
        color_1.grid(row=5, column=0, sticky='ew', pady=self.grid_pad_x)

        color_2 = tk.Radiobutton(self.frame,
                                 variable=self.player_color,
                                 text=self.settings.token_colors[1].title(),
                                 value=1,
                                 background=self.settings.window_color,
                                 activebackground=self.settings.token_colors[1],
                                 highlightbackground=self.settings.window_color)
        color_2.grid(row=5, column=1, sticky='ew', padx=self.grid_pad_x, pady=self.grid_pad_x)

        save_button = ttk.Button(self.frame,
                                 text="Save",
                                 command=self.save_data)
        save_button.grid(row=6, column=0, columnspan=2, pady=self.grid_pad_x)

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
        if self.player_name.get() != '':
            opponent = self.opponent.get().lower()

            game.MODE = {
                'player_1': self.player_name.get(),
                'player_2': opponent if opponent != '-choose opponent-' else 'ai',
                'human_opponent_name': self.opponent_name.get(),
                'player_color_id': self.player_color.get()
            }

            logger.debug("Game mode defined")
            logger.info(f'Game config: {game.MODE}')

            self.on_save()

    def on_opponent_choice(self, event=None) -> None:
        if self.opponent.get() == 'Human':
            self.human_opponent_name.lift()
            self.human_opponent_name_entry.lift()
            self.human_opponent_name_entry.focus_set()
        else:
            self.human_opponent_name.lower(self.frame)
            self.human_opponent_name_entry.lower(self.frame)

    def on_save(self, event=None) -> None:
        logger.info("Popup closed")
        self.destroy()

    def on_exit(self, event=None) -> None:
        self.destroy()
        logger.info("Exit App")
        sys.exit()
