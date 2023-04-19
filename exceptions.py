class EnemyDown(Exception):
    def __init__(self, level) -> None:
        self.level = level


class GameOver(Exception):
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score


