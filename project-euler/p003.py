import eulerlib


def compute(n: int = 600_851_475_143) -> int:
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?

    ed. there's quite a bit of prior work for prime factoring, but I don't remember any of it
    offhand. 6e11 is pretty small, so just working on odd numbers and stopping the brute force search
    at j for j > sqrt(n) allows us to try fewer than a half a million factors
    """

    return max(eulerlib.prime_factors(n))
