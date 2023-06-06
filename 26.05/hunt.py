import random

class Predator:
    def __init__(self, name):
        self.name = name
        self.hunger = 0

    def hunt(self, prey):
        if prey.is_alive:
            print(f'{self.name} полює на {prey.name}!')
            prey.is_alive = False
            self.hunger += 1
            print(f'{self.name} полював на {prey.name} та став ситий ({self.hunger}).')

class Prey:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def flee(self):
        if self.is_alive:
            print(f'{self.name} утік від хижака!')


predator = Predator('Вовк')
prey = Prey('Заяць')


predator.hunt(prey)


prey.flee()
