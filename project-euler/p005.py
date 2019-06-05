import eulerlib


def compute_brute_force(upper_divisor_bound: int = 20) -> int:
    """smallest multiple

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    
    Args:
        upper_divisor_bound (int, optional): Defaults to 20.
    
    Returns:
        int

    232792560
    """

    range_list = unique_divisors(list(range(1, upper_divisor_bound + 1)))

    # well, we know for sure that it's at least the product of all the primes between 1 and upper_divisor_bound
    lower_limit = 1
    for i in eulerlib.primes_between(1, upper_divisor_bound):
        lower_limit *= i

    # Now go down to the nearest multiple of upper_divisor_bound so that we can step by upper_divisor_bound
    # through the search
    lower_limit = lower_limit - (lower_limit % upper_divisor_bound)

    i = lower_limit
    j = 0
    while True:
        if j % 1_000_000 == 0:
            print(f"testing {i}")
        j += 1

        if divideslist(i, range_list):
            return i

        i += upper_divisor_bound


def divideslist(a, b):
    # we can remove factors of numbers in
    for i in b:
        if a % i != 0:
            return False

    return True


def compute_lcm(upper_divisor_bound: int = 20) -> int:
    """
    As I was trying to figure out how to define the lower bound of the numbers to test, I sort
    of stumbled into a way to just calculate it directly

    This just computes the least common multiple of the integers up to upper_divisor_bound
    """

    king_of_lcms = 1
    for i in range(1, upper_divisor_bound + 1):
        king_of_lcms = eulerlib.lcm(i, king_of_lcms)

    return king_of_lcms


def compute(upper_divisor_bound: int = 20) -> int:
    return compute_lcm(upper_divisor_bound)


def unique_divisors(range_list):
    return_list = range_list
    range_list.reverse()
    print(range_list)

    for i, n in enumerate(range_list):
        if i == len(range_list):
            break

        # just remove any smaller number if it divides n
        for j in range_list[i + 1 :]:
            if n % j == 0:
                range_list.remove(j)

    return range_list
