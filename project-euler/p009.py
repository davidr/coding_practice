from typing import List

def compute(sum_of_nums: int = 1000) -> int:
    """special pythagorean triplet


    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    
    Args:
        sum_of_nums (int, optional)

    Returns:
        int
    """
    
    return compute_bruteforce(sum_of_nums)


def compute_bruteforce(sum_of_nums: int) -> int:
    a = 1
    b = a + 1
    c = sum_of_nums - (a + b)

    # precompute the table of squares. This saves us ~70% over computing a^2 + b^2 == c^2 every time
    squares = gen_table_of_squares(sum_of_nums)

    def _is_triplet(a, b, c):
        if squares[a] + squares[b] == squares[c]:
            return True
        return False

    while True:
        if _is_triplet(a, b, c):
            return a * b * c

        # move on to the next set of numbers
        b += 1
        c -= 1

        if b > c:
            # b and c crossed. increment a and start over!
            a += 1
            b = a + 1
            c = sum_of_nums - (a + b)

            if not a < b < c:
                # We're done and didn't find anything. :(
                return None

def gen_table_of_squares(n) -> List[int]:
    return [i**2 for i in range(0,n+1)]