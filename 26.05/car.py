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
            print(f'{self.name} полював на {prey.name} і став голодний ({self.hunger}).')

class Prey:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def flee(self):
        if self.is_alive:
            print(f'{self.name} утік від хижака!')


predator1 = Predator('Лев')
predator2 = Predator('Тигр')
prey1 = Prey('Зебра')
prey2 = Prey('Антилопа')

predator1.hunt(prey1)
predator2.hunt(prey2)


prey1.flee()
prey2.flee()
