import sys

from src import config
from src.logger import logger
from src.models.popup import GameModePopUp
from src.models.window import Window
from src.models.player import HumanPlayer
from src import game

if __name__ == '__main__':
    logger.info("Start App")

    PYTHON_MIN_VERSION: tuple = (3, 10)
    PYTHON_CURRENT_VERSION: tuple = sys.version_info[0:2]

    if PYTHON_CURRENT_VERSION < PYTHON_MIN_VERSION:
        logger.critical("Python version too old to run the app.")
        logger.debug("Exit App")
        sys.exit()

    settings = config.Settings()
    logger.debug("Game settings initialised")
    logger.info(f'{settings}')

    popup = GameModePopUp(settings)
    popup.show()

    window = Window(settings)

    player_1 = HumanPlayer("Yacine", settings.token_colors[0], window)
    player_2 = HumanPlayer("Khaled", settings.token_colors[1], window)

    game.PLAYERS = [player_1, player_2]

    window.run()
