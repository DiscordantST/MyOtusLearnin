from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, max_cargo, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, number):
        if number + self.cargo <= self.max_cargo:
            self.cargo += number
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        remove_carg = self.cargo
        self.cargo = 0
        return remove_carg
