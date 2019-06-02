import eulerlib
import itertools


def compute(number_of_digits: int = 3) -> int:
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of
    two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    Notes:

    This is super slow and doesn't skip all the products that have already been computed
    in reverse (i.e. won't skip xy if yx has been computed), but gives the right answer

    Args:
        digits (int, optional): number of digits in product numbers. Defaults to 3.

    Returns:
        int: largest palindromic product

    """
    largest_palindrome = -1

    digits = eulerlib.n_digit_numbers(number_of_digits)
    for i, j in itertools.product(digits, repeat=2):
        k = i * j
        if eulerlib.is_palindromic(k):
            if k > largest_palindrome:
                largest_palindrome = k

    return largest_palindrome if largest_palindrome != -1 else None
