import sys
import tkinter as tk

from src import config
from src.logger import logger

if __name__ == '__main__':
    PYTHON_MIN_VERSION: tuple = (3, 11)
    PYTHON_CURRENT_VERSION: tuple = sys.version_info[0:2]

    if PYTHON_CURRENT_VERSION < PYTHON_MIN_VERSION:
        logger.critical("Python version too old to run the app.")
        logger.debug("Exit.")
        sys.exit()

    settings = config.Settings(1.1)

    logger.info("ok")
