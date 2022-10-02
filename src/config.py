import sys
from typing import Tuple
from dataclasses import dataclass

from src.logger import logger


class SettingError(Exception):
    pass


@dataclass(init=True, frozen=True)
class Settings:
    board_columns_number: int = 7
    board_rows_number: int = 6
    board_color: str = "blue"
    board_border_thickness: int = 4
    window_title: str = "Crazy Connect 4"
    window_color: str = "darkgrey"
    token_colors: Tuple[str, ...] = ("yellow", "red")
    font_family: str = "Chilanka"

    @property
    def get_number_of_boxes(self) -> int:
        return self.board_columns_number * self.board_rows_number

    def __post_init__(self):
        expected = {
            'board_columns_number': int,
            'board_rows_number': int,
            'board_color': str,
            'board_border_thickness': int,
            'window_title': str,
            'window_color': str,
            'token_colors': tuple,
            'font_family': str,
        }

        for attribute, attr_type in expected.items():
            if not isinstance(getattr(self, attribute), attr_type):
                try:
                    raise SettingError()
                except SettingError:
                    logger.error(f'Wrong setting type: "{attribute}" must be {attr_type}')
                    logger.debug("Exit App")
                    sys.exit()
