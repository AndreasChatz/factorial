import prime_swing
from constants import PRIMES_UP_TO_2017


def test_is_prime():
    test_cases = (
        (1, False),
        (13, True),
        (15, False),
        (8273, True),
        (8279, False),
        (15486101, True),
        (15486127, False),
        (179425261, True),
        (179425291, False),
    )

    for test_case in test_cases:
        number, result = test_case
        assert prime_swing.is_prime(number) == result


def test_all_prime_numbers_up_to_2017():
    for result, primes in zip(prime_swing.all_prime_numbers_up_to(2017),
                              PRIMES_UP_TO_2017):
        assert result == primes


def test_prime_exponents_of_a_swing_number():
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
    test_cases = (
        (3,  [1, 1]),
        (7,  [2, 0, 1, 1]),
        (15, [3, 2, 1, 0, 1, 1]),
        (31, [4, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1]),
        (62, [5, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]),
    )
    for test_case in test_cases:
        swing_number, result = test_case
        prime_numbers = prime_swing.all_prime_numbers_up_to(swing_number)
        assert prime_swing.prime_exponents_of_a_swing_number(
            swing_number, prime_numbers) == result


def test_compute_swinging_factorial():
    test_cases = (
        (3,  2 * 3),
        (7,  2**2 * 5 * 7),
        (15, 2**3 * 3**2 * 5 * 11 * 13),
        (31, 2**4 * 3**2 * 5 * 17 * 19 * 23 * 29 * 31),
        (62, 2**5 * 7 * 11 * 17 * 19 * 37 * 41 * 43 * 47 * 53 * 59 * 61),
    )

    for test_case in test_cases:
        swinging_factorial, result = test_case
        prime_numbers = prime_swing.all_prime_numbers_up_to(swinging_factorial)
        prime_exponents_array = prime_swing.prime_exponents_of_a_swing_number(
            swinging_factorial, prime_numbers)

        assert prime_swing.compute_swinging_factorial(
            prime_numbers, prime_exponents_array) == result


def test_divide_swing_and_conquer():
    test_cases = (
        (0, 1),
        (1, 1),
        (5, 120),
        (6, 720),
        (13, 6227020800),
        (24, 620448401733239439360000),
        (42, 1405006117752879898543142606244511569936384000000000),
        (62, 31469973260387937525653122354950764088012280797258232192163168247821107200000000000000),
        (100, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000),
    )

    for test_case in test_cases:
        number, factorial = test_case
        assert prime_swing.divide_swing_and_conquer(number) == factorial
