from car import Car
from human import Human

vlad = Human("Vlad", 1)
mikita = Human("Mikita", 1)
Illia = Human("Illia", 1)
andrii = Human("Andrii", 0)
bronislav = Human("Bronislav", 0)

Humans = list
humans.append(vlad)
humans.append(mikita)
humans.append(illia)
humans.append(andrii)
humans.append(bronislav)

car = Car("BMW x6m")

for human in humans:
    car.AddPassengers(human)
    car.AddDriver(human)

for passengers in car.Passengers
    passenger.ToStringPassenger(passengers)

for driver in car.Drivers
    car.ToStringDriver(driver)
