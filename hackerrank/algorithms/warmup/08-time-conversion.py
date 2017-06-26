#!/bin/python3

import sys

def timeConversion(s):
    # using datetime seems like cheating
    hour, minute, second = map(int, s[:-2].split(sep=':'))
    suffix = s[-2:]

    if suffix == "PM" and hour != 12:
        hour += 12
    elif suffix == "AM" and hour == 12:
        hour = 00

    return "{:02d}:{:02d}:{:02d}".format(hour, minute, second)

s = input().strip()
result = timeConversion(s)
print(result)

