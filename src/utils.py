"""This module provides some utilities functions used in the program."""

import random
import os
import socket
from datetime import datetime
from typing import Tuple, List

Coords = Tuple[int, int]
Matrix = List[List[int]]

TIME = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
USER_INFO = f'{os.getlogin()}_{socket.gethostbyname(socket.gethostname())}'    # user_ip-address
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


def random_column(columns_number: int) -> int:
    """This function returns a random number between 0 and the board columns number.

    Args:
        columns_number (int): The number of columns in the game board.

    Returns:
        int: a random integer between 0 and columns_number.

    """
    return random.randint(0, columns_number - 1)


def middle(point_1: Coords, point_2: Coords) -> Coords:
    """This function computes and returns the coordinates of the middle of a section, represented by its two endpoints.

    Args:
        point_1 (Tuple[int, int]): The coordinates of the first endpoint of the section.
        point_2 (Tuple[int, int]): The coordinates of the second endpoint of the section.

    Returns:
        Tuple[int, int]: The coordinates of the middle point of the section.

    """
    return (point_2[0] + point_1[0]) // 2, (point_2[1] + point_1[1]) // 2


def transpose(matrix: Matrix) -> Matrix:
    """This function computes the transpose of a given 2D matrix.

    Args:
        matrix (List[List[int]]): A 2D matrix of integers.

    Returns:
        List[List[int]]: The transpose of matrix.

    """
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
