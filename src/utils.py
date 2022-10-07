import random
from typing import Tuple

from src import game


def random_column():
    return random.randint(0, game.SETTINGS.board_columns_number - 1)


def middle(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> Tuple[int, int]:
    return (point_2[0] + point_1[0]) // 2, (point_2[1] + point_1[1]) // 2
