"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __str__(self):
        return f"Exception: Low fuel error"


class NotEnoughFuel(Exception):
    def __str__(self):
        return f"Exception: Not enough fuel"


class CargoOverload(Exception):
    def __str__(self):
        return f"Exception: Car go over load"

