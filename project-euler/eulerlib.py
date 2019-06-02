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
    return range(10 ** (n - 1), 10 ** n)

