#!/bin/python3

import sys


n = int(input().strip())

for i in range(n):
    print('{:s}{:s}'.format(" " * (n-i-1), "#"*(i+1)))
