import random
import setting
import exceptions


class Enemy:
    def __init__(self, level, health) -> None:
        self.level = level
        self.health = health

    def decrease_health(self) -> None:
        self.health -= 1
        if self.health <= 0:
            print('The level of enemy is', self.level)
            raise exceptions.EnemyDown

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
        attack = self.select_attack()
        defence = enemy.select_defence()
        self.result_fight = self.fight(attack, defence)
        print('result_fight: ', self.result_fight)
        if self.result_fight == 'win':
            enemy.decrease_health()
            self.score += setting.SCORE_SUCCESS_ATTACK
            print('YOUR ATTACK IS SUCCESSFUL!', 'enemy_health', enemy.health,
                  'my_health', self.health)
        elif self.result_fight == 'loose':
            print('YOUR ATTACK IS FAILED!', 'enemy_health', enemy.health,
                  'my_health', self.health)
        elif self.result_fight == 'draw':
            print('IT’S A DRAW!', 'enemy_health', enemy.health,
                  'my_health', self.health)

    def decrease_health(self) -> None:
        self.health -= 1
        if self.health <= 0:
            with open('result.txt', 'a') as f:
                f.write(str(self.name) + ' has score: ' + str(self.score) + '\n')
            print('The score of' + str(self.name) + ' is ' + str(self.score))
            raise exceptions.GameOver

    def defence(self, enemy: Enemy) -> None:
        attack = enemy.select_attack()
        defence = self.select_defence()
        self.result_fight = self.fight(attack, defence)
        print('result_fight: ', self.result_fight)
        if self.result_fight == 'win':
            enemy.decrease_health()
            print('YOUR DEFENCE IS SUCCESSFUL!', 'enemy_health', enemy.health,
                  'my_health', self.health)
        elif self.result_fight == 'loose':
            self.decrease_health()
            print('YOUR DEFENCE IS FAILED!', 'enemy_health', enemy.health,
                  'my_health', self.health)
        elif self.result_fight == 'draw':
            print('IT’S A DRAW!', 'enemy_health', enemy.health,
                  'my_health', self.health)

    @staticmethod
    def fight(attack, defence) -> str:
        if attack == defence:
            return 'draw'
        elif attack == 1 and defence == 3 or attack == 2 and defence == 1 \
                or attack == 3 and defence == 2:
            return 'win'
        return 'loose'

    @staticmethod
    def select_attack() -> int:
        choice = 0
        while choice not in ('1', '2', '3'):
            choice = input('Please make your choice to defend, it must be 1,2 or 3 \n \
            WIZARD  = 1, THIEF = 2,  KNIGHT = 3 ')
        return int(choice)

    @staticmethod
    def select_defence() -> int:
        choice = 0
        while choice not in ('1', '2', '3'):
            choice = input('Please make your choice to defend, it must be 1,2 or 3 \n \
            WIZARD  = 1, THIEF = 2,  KNIGHT = 3 ')
        return int(choice)

