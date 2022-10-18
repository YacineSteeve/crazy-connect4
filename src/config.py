from typing import Tuple
from dataclasses import dataclass, fields

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


@dataclass(init=True, eq=True)
class Settings:
    board_columns_number: int = 7
    board_rows_number: int = 6
    board_color: str = "blue"
    board_border_thickness: int = 4
    popup_geometry_scale: float = 0.65
    window_geometry_scale: float = 0.8
    window_title: str = "Crazy Connect 4"
    window_color: str = "darkgrey"
    token_colors: Tuple[str, ...] = ("yellow", "red")
    font_family: str = "Chilanka"

    @property
    def get_number_of_boxes(self) -> int:
        return self.board_columns_number * self.board_rows_number

    def save(self, log=True):
        wrong_setting = False

        for field in fields(self):
            if not isinstance(getattr(self, field.name), type(field.default)):
                wrong_setting = True
                setattr(self, field.name, field.default)
                try:
                    raise SettingError()
                except SettingError:
                    logger.error(f'Wrong setting type: "{field.name}" must be {field.type}')

        if wrong_setting:
            logger.warning("Default settings will be used")

        if log:
            logger.debug("Game settings initialised")
            logger.info(f'{self}')

        return self
