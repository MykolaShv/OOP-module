import random
import setting as setting
import exceptions as exceptions


class Enemy:
    def __init__(self, level, health) -> None:
        self.level = level
        self.health = health

    def decrease_health(self) -> None:
        self.health -= 1
        if self.health <= 0:
            exceptions.EnemyDown.write_to_the_file(self)
            raise exceptions.EnemyDown(self.level)

    @staticmethod
    def select_attack() -> int:
        return random.randint(1, 3)

    @staticmethod
    def select_defence() -> int:
        return random.randint(1, 3)


class Player:
    def __init__(self, name, health, score, result_fight) -> None:
        self.health = health
        self.score = score
        self.name = name
        self.result_fight = result_fight

    def attack(self, enemy: Enemy) -> None:
        result_attack_player = self.select_attack()
        result_defend_enemy = enemy.select_defence()
        print('enemy is', result_defend_enemy)
        result_fight = self.fight(result_attack_player, result_defend_enemy)
        print('result_fight', result_fight)
        if result_fight == setting.RESULT_FIGHTS[0]:
            enemy.decrease_health()
            self.score += setting.SCORE_SUCCESS_ATTACK
            print('YOUR ATTACK IS SUCCESSFUL! Your score is: ', self.score,  'Your health is: ', self.health,
                  'Enemy\'s health is: ', enemy.health, 'Enemy\'s level is: ', enemy.level)
        elif result_fight == setting.RESULT_FIGHTS[1]:
            self.decrease_health()
            print('YOUR ATTACK IS FAILED! Your score is: ', self.score,  'Your health is: ', self.health,
                  'Enemy\'s health is: ', enemy.health, 'Enemy\'s level is: ', enemy.level)
        elif result_fight == setting.RESULT_FIGHTS[2]:
            self.score += setting.SCORE_DRAW_ATTACK
            print('IT’S A DRAW! Your score is: ', self.score,  'Your health is: ', self.health,
                  'Enemy\'s health is: ', enemy.health, 'Enemy\'s level is: ', enemy.level)

    def decrease_health(self) -> None:
        self.health -= 1
        if self.health <= 0:
            exceptions.GameOver.write_to_the_file(self)
            raise exceptions.GameOver(self.name, self.score)

    def defence(self, enemy: Enemy) -> None:
        result_defence_player = self.select_defence()
        result_attack_enemy = enemy.select_attack()
        print('enemy is', result_attack_enemy)
        self.result_fight = self.fight(result_defence_player, result_attack_enemy)
        if self.result_fight == setting.RESULT_FIGHTS[0]:
            enemy.decrease_health()
            self.score += setting.SCORE_SUCCESS_ATTACK
            print('YOUR DEFENCE IS SUCCESSFUL! Your score is: ', self.score,  'Your health is: ', self.health,
                  'Enemy\'s health is: ', enemy.health, 'Enemy\'s level is: ', enemy.level)
        elif self.result_fight == setting.RESULT_FIGHTS[1]:
            self.decrease_health()
            print('YOUR DEFENCE IS FAILED!Your score is: ', self.score,  'Your health is: ', self.health,
                  'Enemy\'s health is: ', enemy.health, 'Enemy\'s level is: ', enemy.level)
        elif self.result_fight == setting.RESULT_FIGHTS[2]:
            self.score += setting.SCORE_DRAW_ATTACK
            print('IT’S A DRAW!Your score is: ', self.score,  'Your health is: ', self.health,
                  'Enemy\'s health is: ', enemy.health, 'Enemy\'s level is: ', enemy.level)

    @staticmethod
    def fight(attack, defence) -> str:
        if attack == defence:
            print('attack, defence',attack, defence)
            return setting.RESULT_FIGHTS[2]
        elif attack == 1 and defence == 3 or attack == 2 and defence == 1 \
                or attack == 3 and defence == 2:
            print('attack, defence',attack, defence)
            return setting.RESULT_FIGHTS[0]
        print('attack, defence',attack, defence)
        return setting.RESULT_FIGHTS[1]

    def select_attack(self) -> int:
        choice = int(input('Please make your choice to attack, it must be 1,2 or 3 '))
        if choice in (1, 2, 3):
            print('You have chosen: ', setting.ITEMS[choice-1])
            return choice
        else:
            print('your choice is wrong, it must be 1,2 or 3')
            self.select_attack()

    def select_defence(self) -> int:
        choice = int(input('Please make your choice to defend, it must be 1,2 or 3 '))
        if choice in (1, 2, 3):
            print('You have chosen: ', setting.ITEMS[choice-1])
            return choice
        else:
            print('your choice is wrong, it must be 1,2 or 3')
            self.select_defence()
