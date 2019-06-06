import eulerlib

def compute(n: int = 2_000_000) -> int:
    return sum(eulerlib.primes_between(2, n))