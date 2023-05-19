class Car:
    def __init__(self, model, year, brand):
        self.Model = model
        self.Year = year
        self.Brand = brand

    def ShowInfo(self):
            print(f"Model: {self.Model}\n"
             f"Year: {self.Year}\n"
             f"Brand: {self.Brand}")