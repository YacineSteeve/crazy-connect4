from src.logger import logger


class Player:
    def __init__(self, name: str, color: str, window):
        self.name = name
        self.color = color
        self.window = window


class HumanPlayer(Player):
    def __init__(self, player_name: str, color: str, window):
        super().__init__(player_name, color, window)
        ...


class AIPlayer(Player):
    def __init__(self, ai, color: str, window):
        super().__init__(ai.name, color, window)
        ...
