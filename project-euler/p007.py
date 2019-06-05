import eulerlib

def compute(nth_prime: int=10_001) -> int:
    """return the nth prime

    There must be a more elegant way to do this, but this works in ~13s
    
    Args:
        nth_prime (int, optional): number n. Defaults to 10_001.
    
    Returns:
        int
    """
    prime_idx = 0
    n = 2
    while True:
        if eulerlib.is_prime(n):
            prime_idx += 1

        if prime_idx == nth_prime:
            return n

        n += 1
