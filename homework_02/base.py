from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload


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
        if not self.started and self.fuel > 0:
            self.started = True
        else:
            return LowFuelError()

    def move(self):
        pass

# Чтобы рассчитать расход топлива автомобиля, нужно израсходованное топливо поделить на пройденное расстояние,
# а число которое у вас выйдет нужно затем помножить на 100. Если автомобиль израсходовал
# 28 литров бензина на 200 километров дороги, то расчеты будут иметь следующий вид: 28/200 x 100 = 14 л/100 км.1
