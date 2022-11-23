"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return list([i ** 2 for i in args])  # search i in list of number and square it. for (1, 2, 4, 5) return as list
    # [2, 4, 8, 10]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(i):  # filter PRIME number
    k = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


def filter_numbers(digit, filter_type):  # digigt as [1, 2, 3, 4]; filter_type as ODD; EVEN; PRIME
    if filter_type == ODD:
        return [i for i in digit if i % 2 != 0]
    if filter_type == EVEN:
        return [i for i in digit if i % 2 == 0]
    if filter_type == PRIME:
        return [i for i in digit if is_prime(i) is True and i > 1]