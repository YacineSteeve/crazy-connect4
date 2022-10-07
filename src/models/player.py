class HumanPlayer:
    def __init__(self, player_name: str, color: str, window):
        self.name = player_name[:15]
        self.color = color
        self.window = window


class AIPlayer:
    def __init__(self, ai, color: str, window):
        self.ai = ai
        self.name = ai.name[:15]
        self.color = color
        self.window = window

    def move(self) -> int:
        return self.ai.move()
