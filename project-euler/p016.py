def compute(power: int = 1000) -> int:
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?

    I might have cheated on p015, but python cheats on p016. Thank you, arbitrary precision integer type
    
    Args:
        power (int, optional): n-th power of 2 whose digits to sim. Defaults to 1000.
    
    Returns:
        int: sum of all digits of 2^n
    """

    n = 2 ** power
    return sum([int(i) for i in str(n)])