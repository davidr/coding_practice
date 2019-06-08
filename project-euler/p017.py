import eulerlib


def compute(n: int = 1000) -> int:
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
    3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used? 

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
    23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing
    out numbers is in compliance with British usage.
    
    Args:
        n (int, optional): numbers up to n. Defaults to 1000.
    
    Returns:
        int
    """

    string_length = 0
    for i in range(1, n + 1):
        string_length += len(
            eulerlib.number_to_english(i).replace(" ", "").replace("-", "")
        )
    return string_length
