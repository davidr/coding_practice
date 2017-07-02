#!/usr/bin/env python3.6


def listlessthanten():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [x for x in a if x < 5]
    print(b)

def divisors_div(n):
    divisors = []
    for i in range(2, n):
        if n/i == n//i:
            divisors.append(i)

    if len(divisors) == 0:
        print(f'{n:d} is prime')
    else:
        print(f'{divisors}')

def divisors_mod(n):
    divisors = []
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)

    if len(divisors) == 0:
        print(f'{n:d} is prime')
    else:
        print(f'{divisors}')

def list_overlap(a, b):
    overlap = [x for x in a if x in b]
    overlap += [x for x in b if x in a]
    print(set(overlap))

def list_overlap_set(a, b):
    a = set(a)
    b = set(b)
    print(a.intersection(b))

def is_palindrome(s):
    # start one index at the beginning and another at the end
    i = 0
    j = len(s) - 1

    while i < j:
        if i == j:
            break
        if s[i] != s[j]:
            return(False)
        i += 1
        j -= 1

    return(True)

def fibonacci_recurse(n):
    """Return the nth Fibonacci number"""
    if n in (1, 2):
        return(1)
    else:
        return(fibonacci_recurse(n-1) + fibonacci_recurse(n-2))

def fibonacci_norecurse(n):
    """Return the nth Fibonacci number without recursion"""
    if n in (1, 2):
        return(1)
    else:
        # start with the 3rd number and work our way up
        penultimate = 1
        ultimate = 1

        for i in range(3, n+1):
            fibonacci = penultimate + ultimate
            penultimate = ultimate
            ultimate = fibonacci

        return(fibonacci)


if __name__ == "__main__":
    print(fibonacci_norecurse(7))

