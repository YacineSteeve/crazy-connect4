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

    # Initialize game settings
    settings = config.Settings()
    settings.save()

    popup = GameModePopUp()
    popup.show()

    # Generate a file to save the game stats.
    with open('games.csv', 'w') as file:
        head = ','.join(f'Move{i}' for i in range(1, settings.get_number_of_boxes + 1))
        head += ',Winner\n'
        file.write(head)

    # Launch the game after the popup window is closed
    game.init()
