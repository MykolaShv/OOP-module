class EnemyDown(Exception):
    def __init__(self, level) -> None:
        self.level = level

    def write_to_the_file(self) -> None:
        with open('result.txt', 'a') as f:
            f.write('You have won.  The enemy level is: ' + str(self.level) + '\n')


class GameOver(Exception):
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score

    def write_to_the_file(self) -> None:
        with open('result.txt', 'a') as f:
            f.write('you have lost. The score is ' + str(self.score) + '\n')
