import sys
from typing import Tuple
from dataclasses import dataclass

from src.logger import logger

TITLE_POS_Y_SCALE_REL_TO_HEIGHT = 0.05
TITLE_HEIGHT_SCALE_REL_TO_HEIGHT = 2 * TITLE_POS_Y_SCALE_REL_TO_HEIGHT
TITLE_WIDTH_SCALE_REL_TO_WIDTH = 0.45
TITLE_POS_X_SCALE_REL_TO_WIDTH = (1 - TITLE_WIDTH_SCALE_REL_TO_WIDTH) / 2

BOARD_POS_X_SCALE_REL_TO_WIDTH = 0.05
BOARD_POS_Y_SCALE_REL_TO_HEIGHT = TITLE_HEIGHT_SCALE_REL_TO_HEIGHT + (2 * TITLE_POS_Y_SCALE_REL_TO_HEIGHT)
BOARD_SIZE_SCALE = 1 - TITLE_HEIGHT_SCALE_REL_TO_HEIGHT - (3 * TITLE_POS_Y_SCALE_REL_TO_HEIGHT)


class SettingError(Exception):
    pass


@dataclass(init=True, frozen=True)
class Settings:
    board_columns_number: int = 7
    board_rows_number: int = 6
    board_color: str = "blue"
    board_border_thickness: int = 4
    popup_geometry_scale: float = 0.5
    window_geometry_scale: float = 0.8
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
