class Returnin:
    def __iter__(self):

        return self.generator()

    def generator(self):

        for i in range(5):
            yield i


my_returnin = Returnin()


for value in my_returnin:
    print(value)