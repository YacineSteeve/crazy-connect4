from src import game, utils


class RandomAI:
    def __init__(self):
        self.name = 'Random AI'

    def move(self) -> int:

        column = utils.random_column()

        if len(game.FILLED_BOXES) == 0:
            return column

        if column not in game.FILLED_BOXES:
            return column

        while column in game.FILLED_BOXES and game.FILLED_BOXES[column][-1] == 0:
            column = utils.random_column()

        return column
