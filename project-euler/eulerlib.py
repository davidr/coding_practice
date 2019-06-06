from typing import List, Iterator
from math import sqrt

primes_below_100 = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]


def is_prime_v1(n: int) -> bool:
    """return True if n is prime, else False

    DEPRECATED

    Args:
        n (int): input

    Returns:
        bool
    """

    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    # We only need to check odd numbers, and we can stop once we get to sqrt(n)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def is_prime_v2(n: int) -> bool:
    """is n prime

    implementing the 6k +/- 1 optimization
    
    Args:
        n (int): number to check
    
    Returns:
        bool: True if n is prime, else False
    """
    if n == 1:
        return False
    elif n in (2, 3):
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    # quick check to use tiny precomputed list of primes weed out lots of nonprimes:
    for p in primes_below_100:
        if n % p == 0:
            return False

    for i in range(101, int(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


# This and the next function boosted from rosettacode
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True  # n  is definitely composite


def is_prime_miller_rabin(n, _precision_for_huge_n=16):
    if n in primes_below_100:
        return True
    if any((n % p) == 0 for p in primes_below_100) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(
        _try_composite(a, d, n, s) for a in primes_below_200[:_precision_for_huge_n]
    )


def is_prime(n):
    return is_prime_v2(n)


def primes_between(a: int, b: int) -> Iterator[int]:
    """primes between a and b, inclusive
    
    Args:
        a (int): lower bound
        b (int): upper_bound
    
    Raises:
        ValueError: a > b
    
    Yields:
        int: next prime between a and b
    """
    if a > b:
        raise ValueError("a > b")

    for x in range(a, b + 1):
        if is_prime(x):
            yield x


def gcd(a: int, b: int) -> int:
    """greatest common divisor 
    
    Args:
        a (int)
        b (int)
    
    Returns:
        int: gcd of a, b
    """
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """least common multiple
    
    Args:
        a (int): a
        b (int): b
    
    Returns:
        int: least common multiple of a, b
    """

    return (a * b) // gcd(a, b)


def prime_factors(n: int) -> List[int]:
    # If n is 2, then 2 is the only prime factor of 2. This allows us to start iterating at 3,
    # further allowing us to skip even numbers
    if n == 2:
        return [2]
    factors = []

    for i, j in enumerate(range(3, n, 2)):
        # for some number x, if x is not a factor of n, then no number > n/x will be a
        # factor of x either

        if n % j == 0:
            if is_prime(j):
                factors.append(j)
        elif j > n / j:
            break

    return factors


def is_palindromic(n: int) -> bool:
    str_n = str(n)
    len_n = len(str_n)

    for i in range(len(str_n)):
        j = len_n - 1 - i

        if i >= j:
            break

        if str_n[i] != str_n[j]:
            return False
    return True


def n_digit_numbers(n: int) -> Iterator[int]:
    """return an iterator of all the numbers with n digits
    
    Args:
        n (int): number of digits
    
    Returns:
        Iterator[int]
    """
    return range(10 ** (n - 1), 10 ** n)


def square_of_sums(nums: Iterator[int]) -> int:
    """square of sums
    
    Args:
        nums (Iterator[int]): iterator of integers
    
    Returns:
        int
    """
    return sum(nums) ** 2


def sum_of_squares(nums: Iterator[int]) -> int:
    """sum of squares
    
    Args:
        nums (Iterator[int]): iterator of integers
    
    Returns:
        int
    """
    return sum(map(lambda x: x ** 2, nums))

