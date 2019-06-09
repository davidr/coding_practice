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


def factors(n: int, count_self=True) -> List[int]:
    """factors of n
    
    Args:
        n (int): number to factorisze
        count_self (bool): count self in factors? Defaults to True
    
    Returns:
        List[int]: list of factors of n

    Returns:
        [type]: [description]
    """

    # shortcut some small factors so we don't have to add logic into the computation below
    if n == 1:
        return [1]
    elif n == 2:
        return [1] + ([2] if count_self == True else [])
    elif n == 3:
        return [1] + ([3] if count_self == True else [])
    elif n == 4:
        return [1, 2] + ([4] if count_self == True else [])

    factors = [1]
    test_to = n
    for i in range(2, int(n // 2) + 1):
        if i >= test_to:
            break

        if n % i == 0:
            # i is a factor of n which means that n/i is also a factor
            factors.append(i)
            factors.append(n // i)
            test_to = n // i

    if count_self:
        factors.append(n)
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


def triangle_numbers() -> int:
    """generate the nth triangle number
    
    Args:
        n (int)
    
    Yields:
        int
    """

    triangle_number = 0
    num = 1
    while True:
        triangle_number += num
        yield triangle_number
        num += 1


collatz_cache = {}


def collatz_sequence(starting_number: int, cache: bool = False) -> List[int]:
    sequence = [starting_number]

    n = starting_number
    while n != 1:
        if cache:
            if n in collatz_cache:
                return sequence + collatz_cache[n][1:]

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        sequence.append(n)

    if cache:
        collatz_cache[starting_number] = sequence
    return sequence


# fmt: off
_number_strings_by_one = [
    "zero",    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
    "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

_number_strings_by_ten = [
    None, "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
]
# fmt: on


def number_to_english(n: int) -> str:
    """given nonnegative integer n, return a string of n written out in english
    
    Args:
        n (int): some integer

    Raises:
        ValueError: if we don't go up to the number requested
    
    Returns:
        str
    """

    if 0 <= n < 20:
        return _number_strings_by_one[n]
    elif n < 100:
        ones = n % 10
        tens = (n - ones) // 10
        return _number_strings_by_ten[tens] + (
            "-" + number_to_english(ones) if ones != 0 else ""
        )
    elif n < 1000:
        tens = n % 100
        hundreds = (n - tens) // 100
        return _number_strings_by_one[hundreds] + " hundred" + (
            " and " + number_to_english(tens) if tens != 0 else ""
        )
    elif n < 1_000_000:
        hundreds = n % 1000
        thousands = (n - hundreds) // 1000
        return number_to_english(thousands) + " thousand" + (
            " and " + number_to_english(hundreds) if hundreds != 0 else ""
        )

    raise ValueError("we don't go up that high")


def ordinal_value_ofletter(letter: str) -> int:
    """return the ordinal value of the letter a

    ex: ordinal_value_ofletter(a) = 1, b = 2...
    
    Args:
        letter (str): a letter of the alphabet

    Raises:
        ValueError: if a is not a single letter
    
    Returns:
        int: ordinal value of a
    """

    if len(letter) > 1 or not letter.isalpha():
        raise ValueError(f"{letter} must be a single letter")

    return 1 + ord(letter.lower()) - ord('a')