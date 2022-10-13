import sys
import os

from src import config
from src.logger import logger
from src.models.popup import GameModePopUp
from src.models.window import Window
from src.models.player import HumanPlayer, AIPlayer
from src.models.ai import RandomAI
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
    settings.save()

    logger.debug("Game settings initialised")
    logger.info(f'{game.SETTINGS}')

    popup = GameModePopUp()
    popup.show()

    window = Window()

    player_1 = HumanPlayer(player_name=game.MODE.get('player_1', 'Player 1'),
                           color=game.SETTINGS.token_colors[game.MODE.get('player_color_id', 0)],
                           window=window)

    if game.MODE.get('player_2') == 'human':
        player_2 = HumanPlayer(player_name=game.MODE.get('human_opponent_name', 'Player 2'),
                               color=game.SETTINGS.token_colors[not game.MODE.get('player_color_id', 0)],
                               window=window)
    else:
        player_2 = AIPlayer(ai=RandomAI(),
                            color=game.SETTINGS.token_colors[not game.MODE.get('player_color_id', 0)],
                            window=window)

    game.PLAYERS = [player_1, player_2]

    game.BOXES_MATRIX = [
        [game.EMPTY for _ in range(game.SETTINGS.board_columns_number)]
        for _ in range(game.SETTINGS.board_rows_number)
    ]

    game.IS_PLAYING = True

    game.SOUNDS['token'] = os.path.abspath('ressources/token-sound.mp3')

    window.run()
