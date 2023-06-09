import models
import setting
import exceptions


def get_player_name() -> str:
    name = ''
    while not name:
        name = input('Please input your name ').strip()
    return name


def play() -> None:
    enemy = models.Enemy(level=setting.INITIAL_ENEMY_LEVEL, health=setting.INITIAL_ENEMY_HEALTH)
    player = models.Player(name=get_player_name(), health=setting.INITIAL_PLAYER_HEALTH,
                           score=setting.INITIAL_PLAYER_SCORE, result_fight=0)
    game_round = 0
    while True:
        try:
            player.attack(enemy)
            game_round += 1
            print('round = ', game_round)
            player.defence(enemy)
            game_round += 1
            print('round = ', game_round)
        except exceptions.EnemyDown:
            enemy = models.Enemy(enemy.level + 1, enemy.health)
        except exceptions.GameOver:
            break


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print('you are off')
