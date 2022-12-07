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


#Constants that determine which scenario the calculation will follow
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def prime_number(digit_from_sequence):
    """
    A prime number is an integer that is only divisible by 1 and by itself without a remainder
    info about prime numbers https://en.wikipedia.org/wiki/List_of_prime_numbers)
    :param digit_from_sequence: sequence number
    :return: True if digit is PRIME
    """
    count = 0
    for elem in range(2, digit_from_sequence // 2 + 1):
        if digit_from_sequence % elem == 0:
            count += 1
    if count <= 0 and digit_from_sequence > 1:
        return True


def odd_number(digit_from_sequence):
    """
    An odd number is an integer that is not divisible by 2 without a remainder
    :param digit_from_sequence: sequence number
    :return: True if elem is ODD
    """
    if digit_from_sequence % 2 != 0:
        return True


def even_number(digit_from_sequence):
    """
    An even number is an integer that is divisible by 2 without a remainder
    :param digit_from_sequence: sequence number
    :return: True if elem is EVEN
    """
    if digit_from_sequence % 2 == 0:
        return True


def filter_numbers(sequence, filter_type):
    """
    A function that receives a sequence of natural numbers and, depending on the filter_type,
    gives a list of numbers (even, odd, or prime) as an output
    :param sequence: number sequence integer. example 1, 2, 3, 4, 5, 6, 7
    :param filter_type: ODD/EVEN/PRIME digit. example: filter_type == ODD or filter_type == EVEN or filter_type == PRIME
    :return: list of integer digits. (even, odd, or prime) example: [2, 4, 6]
    """
    if filter_type == ODD:
        odd_number_list = filter(odd_number, sequence)
        return list(odd_number_list)
    if filter_type == EVEN:
        even_number_list = filter(even_number, sequence)
        return list(even_number_list)
    if filter_type == PRIME:
        prime_number_list = filter(prime_number, sequence)
        return list(prime_number_list)

