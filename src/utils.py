import random
import os
import socket
from datetime import datetime
from typing import Tuple, List

Coords = Tuple[int, int]
Matrix = List[List[int]]

TIME = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
USER_INFO = f'{os.getlogin()}.{socket.gethostbyname(socket.gethostname())}'
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


def random_column(columns_number):
    return random.randint(0, columns_number - 1)


def middle(point_1: Coords, point_2: Coords) -> Coords:
    return (point_2[0] + point_1[0]) // 2, (point_2[1] + point_1[1]) // 2


def transpose(matrix: Matrix) -> Matrix:
    n, m = len(matrix), len(matrix[0])

    return [[matrix[i][j] for i in range(n)] for j in range(m)]
