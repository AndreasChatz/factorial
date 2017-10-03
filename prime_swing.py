# https://oeis.org/A000142/a000142.pdf

import math
from typing import List


def divide_swing_and_conquer(number: int, prime_numbers: int) -> int:

    if number == 1:
        return 1

    k = math.floor(math.log2(number))

    prime_factors_exponent_array = prime_factors_exponent(k, number, prime_numbers)

    sf = compute_swinging_factorial(prime_numbers, prime_factors_exponent_array)

    return divide_swing_and_conquer(number//2, prime_numbers)**2 * sf


def prime_factors_exponent(k: int, number: int, prime_numbers: List[int]) -> List[int]:
    prime_factors_exponent_array = []

    for prime in prime_numbers:
        exponent = 0
        for i in range(1, k+1):
            exponent += number // prime ** i % 2
        prime_factors_exponent_array.append(exponent)

    return prime_factors_exponent_array


def compute_swinging_factorial(prime_numbers: List[int], prime_factors_exponent_array: List[int]) -> int:
    swing_factorial = 1
    for prime, factor in zip(prime_numbers, prime_factors_exponent_array):
        if factor == 0:
            continue

        swing_factorial *= prime ** factor
    return swing_factorial


def is_prime(n: int) -> bool:
    """
    Checks if a number is prime or not
    :param n: any positive whole number
    :return: True if the number is prime False otherwise
    """
    if n == 1:
        return False

    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for divisor in range(3, max_divisor+1, 2):
        if n % divisor == 0:
            return False
    return True


def all_prime_numbers_up_to(n: int) -> List[int]:
    """
    Calculates all the prime numbers up to a given number
    :param n: any positive whole number
    :return: all the prime numbers up to a given number as a list
    """
    prime_numbers_array = []
    for num in range(1, n+1):
        if is_prime(num):
            prime_numbers_array.append(num)

    return prime_numbers_array


if __name__ == "__main__":
    try:
        n = int(input('Factorial of: '))
        prime_numbers_array = all_prime_numbers_up_to(n)
        print(divide_swing_and_conquer(n, prime_numbers_array))
    except ValueError:
        print('Please provide an integer')