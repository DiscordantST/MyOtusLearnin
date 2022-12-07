"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*sequence):
    """
    A function that takes N integers and returns a list of squares of those integers
    :param sequence: Sequence integers digit. example: (1,2,3,4,5,6)
    :return: List of square integers digit. example: [1, 4, 9, 16, 25, 36]
    """
    return [digit ** 2 for digit in sequence]


"""
Constants that determine which scenario the calculation will follow
"""
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(digit):
    """

    :param digit: PRIME digit
    :return: True if digit is PRIME, False is digit is not PRIME
    """
    count = 0
    for elem in range(2, digit // 2 + 1):
        if digit % elem == 0:
            count += 1
    if count <= 0:
        return True


def filter_numbers(sequence, filter_type):
    """
    A function that receives a sequence of natural numbers and, depending on the filter_type,
    gives a list of numbers (even, odd, or prime) as an output
    An even number is an integer that is divisible by 2 without a remainder
    An odd number is an integer that is not divisible by 2 without a remainder
    A prime number is an integer that is only divisible by 1 and by itself without a remainder

    :param sequence: number sequence integer. example 1, 2, 3, 4, 5, 6, 7
    :param filter_type: ODD/EVEN/PRIME digit. example: filter_type == ODD or filter_type == EVEN or filter_type == PRIME
    :return: list of integer digits. (even, odd, or prime) example: [2, 4, 6]
    """
    if filter_type == ODD:
        return [digit for digit in sequence if digit % 2 != 0]
    if filter_type == EVEN:
        return [digit for digit in sequence if digit % 2 == 0]
    if filter_type == PRIME:
        return [digit for digit in sequence if is_prime(digit) is True and digit > 1]
