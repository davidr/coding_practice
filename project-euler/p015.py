import math

def compute(n: int = 20) -> int:
    """
    So I cheated and saw that this was a well-known combinatorial problem. For an n x n grid,
    the answer is 2n choose n.
    
    Args:
        n (int, optional): n by n grid. Defaults to 20.
    """

    return math.factorial(2 * n) // (math.factorial(n) * math.factorial(n))