#!/usr/bin/env python3


def simpleArraySum(n, ar):
    # They're unspecific what they want to happen if len(ar) != n. Just return None
    if n == len(ar):
        return(sum(ar))


def solve(a0, a1, a2, b0, b1, b2):
    from collections import Counter
    score = Counter()

    a = [a0, a1, a2]
    b = [b0, b1, b2]

    for alice, bob in zip(a, b):
        if alice > bob:
            score['alice'] += 1
        elif alice < bob:
            score['bob'] += 1

    return score['alice'], score['bob']]


def aVeryBigSum(n, ar):
    # They're unspecific what they want to happen if len(ar) != n. Just return None
    if n == len(ar):
        return(sum(ar))


