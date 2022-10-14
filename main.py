import sys

from src import game, config
from src.logger import logger
from src.models.popup import GameModePopUp

if __name__ == '__main__':
    logger.info("Start App")

    PYTHON_MIN_VERSION: tuple = (3, 10)
    PYTHON_CURRENT_VERSION: tuple = sys.version_info[0:2]

    if PYTHON_CURRENT_VERSION < PYTHON_MIN_VERSION:
        logger.critical("Python version too old to run the app.")
        logger.debug("Exit App")
        sys.exit()

    settings = config.Settings()
    settings.save()

    popup = GameModePopUp()
    popup.show()

    game.init()
