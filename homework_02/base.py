from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """Check self.started and check self.fuel if started is False and fuel > 0
            switch self.started = True, else return LowFuelError"""
        if not self.started:
            if self.fuel:
                self.started = True
            else:
                raise LowFuelError()

    def move(self, distance):
        """
        Method calculates whether the car has enough fuel for the
        trip and update self.fuel
        if there is not enough fuel we return an error NotEnoughFuel
        :param distance: the distance the car has to travel
        """
        fuel = distance / self.fuel_consumption
        if fuel <= self.fuel:
            self.fuel -= fuel
        else:
            raise NotEnoughFuel()







#
# - добавьте метод `move`, который проверяет,
#       что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода),
#       и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
