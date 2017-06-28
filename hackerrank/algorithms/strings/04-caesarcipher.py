#!/bin/python3

import string
import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

s = list(s)

for i, char in enumerate(s):
    if char.islower():
        case = lower
    elif char.isupper():
        case = upper
    else:
        # Not a letter; no need to replace.
        continue

    char_number = case.index(s[i])
    char_number += k
    char_number %= 26

    s[i] = case[char_number]

print("".join(s))
