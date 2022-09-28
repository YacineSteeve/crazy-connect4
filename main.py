import sys


from src import config
import tkinter as tk

if __name__ == '__main__':
    PYTHON_MIN_VERSION: tuple = (3, 10)

    if sys.version_info[0:2] < PYTHON_MIN_VERSION:
        sys.exit('Python version too old')

    settings = config.Settings(1.1)

    print("ok")