import eulerlib

def compute(upper_bound: int = 10000) -> int:
    """sum of amicable numbers under upper_bound

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
    amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

    Args:
        upper_bound (int, optional): compute the sum of amicable numbers under upper_bound. Defaults to 1000.
    
    Returns:
        int

    """

    def d(n: int) -> int:
        return sum(eulerlib.factors(n, count_self=False))

    amicable_numbers = []
    for i in range(1, upper_bound):
        a = i
        b = d(a)

        if a == b or a in amicable_numbers:
            continue

        if d(b) == a:
            amicable_numbers += [a, b]

    return(sum(amicable_numbers))