from typing import List, Iterator


def is_prime(n: int) -> bool:
    """return True if n is prime, else False

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

    for i in range(3, n, 2):
        if n % i == 0:
            return False

    return True


def primes_between(a: int, b: int) -> List[int]:
    if a > b:
        raise ValueError("a > b")

    primes = []

    for x in range(a, b + 1):
        if is_prime(x):
            primes.append(x)

    return primes


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
    return sum(nums)**2

def sum_of_squares(nums: Iterator[int]) -> int:
    """sum of squares
    
    Args:
        nums (Iterator[int]): iterator of integers
    
    Returns:
        int
    """
    return sum(map(lambda x: x**2, nums))