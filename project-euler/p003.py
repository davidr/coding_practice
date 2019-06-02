def _isprime(n: int) -> bool:
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


def compute(n: int = 600_851_475_143) -> int:
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?

    ed. there's quite a bit of prior work for prime factoring, but I don't remember any of it
    offhand. 6e11 is pretty small, so just working on odd numbers and stopping the brute force search
    at j for j > sqrt(n) allows us to try fewer than a half a million factors
    """

    # If n is 2, then 2 is the only prime factor of 2. This allows us to start iterating at 3,
    # further allowing us to skip even numbers
    if n == 2:
        return [2]

    prime_factors = []

    for i, j in enumerate(range(3, n, 2)):
        # print status
        if i % 1_000 == 0:
            print(f"reached {j:,}: {prime_factors}")

        # for some number x, if x is not a factor of n, then no number > n/x will be a
        # factor of x either

        if n % j == 0:
            if _isprime(j):
                prime_factors.append(j)
        elif j > n / j:
            print(f"breaking at {j}")
            break

    return max(prime_factors)
