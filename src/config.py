from dataclasses import dataclass
from src.logger import SettingError
from typing import Tuple


@dataclass(init=True, repr=True, frozen=True)
class Settings:
    board_columns_number: int = 7
    board_rows_number: int = 6
    window_title: str = "Crazy Connect 4"
    token_colors: Tuple[str] = ("yellow", "red")

    @property
    def get_number_of_boxes(self) -> int:
        return self.board_columns_number * self.board_rows_number

    def __post_init__(self):
        ...
