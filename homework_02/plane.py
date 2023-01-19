from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, number):
        if number + self.cargo <= self.max_cargo:
            self.cargo += number
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        remove_cargo = self.cargo
        self.cargo = 0
        return remove_cargo
