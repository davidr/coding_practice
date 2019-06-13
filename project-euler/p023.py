import eulerlib


def compute() -> int:
    """non-abundant sums

    A perfect number is a number for which the sum of its proper divisors is exactly equal to the
    number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which
    means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called
    abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
    written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
    all integers greater than 28123 can be written as the sum of two abundant numbers. However, this
    upper limit cannot be reduced any further by analysis even though it is known that the greatest
    number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

    Returns:
        int
    """
    upper_bound = 28123

    abundant_numbers = []
    for n in range(1, upper_bound + 1):
        if _is_abundant(n):
            abundant_numbers.append(n)

    # There must be some trick here, but I can't think of anything better than summing all the
    # numbers in abundant_numbers
    abundant_sums = set()
    for i, a in enumerate(abundant_numbers):
        for b in abundant_numbers[i:]:
            n = a + b
            if n < upper_bound + 1:
                abundant_sums.add(n)

    #sums = set(abundant_sums)
    allnums = set(range(1, upper_bound + 1))

    return sum(allnums.difference(abundant_sums))


def _is_abundant(n: int) -> bool:
    return n < sum(eulerlib.factors(n, count_self=False))
