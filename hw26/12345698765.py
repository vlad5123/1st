class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Mammal(Animal):
    def nurse(self):
        pass


class Reptile(Animal):
    def lay_eggs(self):
        pass


class Platypus(Mammal, Reptile):
    def __init__(self, name):
        super().__init__(name)