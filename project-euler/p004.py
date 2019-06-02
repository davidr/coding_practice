import itertools

from typing import Iterator


def _is_palindromic(n: int) -> bool:
    str_n = str(n)
    len_n = len(str_n)

    for i in range(len(str_n)):
        j = len_n - 1 - i

        if i >= j:
            break

        if str_n[i] != str_n[j]:
            return False
    return True


def _n_digit_numbers(n: int) -> Iterator[int]:
    return range(10 ** (n - 1), 10 ** n)


def compute(number_of_digits: int = 3) -> int:
    """largest palindrome product

    This is super slow and doesn't skip all the products that have already been computed
    in reverse (i.e. won't skip xy if yx has been computed), but gives the right answer
    
    Args:
        digits (int, optional): number of digits in product numbers. Defaults to 3.
    
    Returns:
        int: largest palindromic product

    """
    largest_palindrome = -1

    digits = _n_digit_numbers(number_of_digits)
    for i, j in itertools.product(digits, repeat=2):
        k = i * j
        if _is_palindromic(k):
            if k > largest_palindrome:
                largest_palindrome = k

    return largest_palindrome
