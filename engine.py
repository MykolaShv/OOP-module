import models as models
import setting as setting


def get_player_name() -> str:
    name = str(input('Please input your name ')).strip()
    if name:
        return name
    else:
        print('Write smth')
        get_player_name()


def play() -> None:
    enemy = models.Enemy(level=setting.INITIAL_ENEMY_LEVEL, health=setting.INITIAL_ENEMY_HEALTH)
    player = models.Player(name=get_player_name, health=setting.INITIAL_PLAYER_HEALTH,
                           score=setting.INITIAL_PLAYER_SCORE, result_fight=0)
    game_round = 0
    while True:
        player.attack(enemy)
        game_round += 1
        print('round = ', game_round)
        while player.result_fight == setting.RESULT_FIGHTS[0]:
            print('player.result_fight = ', player.result_fight)
            enemy.level += 1
            game_round += 1
            print('round = ', game_round)
            player.attack(enemy)
        player.defence(enemy)
        game_round += 1
        print('round = ', game_round)


if __name__ == '__main__':
    get_player_name()
    try:
        play()
    except KeyboardInterrupt:
        print('you are off')
