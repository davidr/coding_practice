#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

# Iterate by row, keeping a running count
pri_diag = 0
sec_diag = 0

for i in range(n):
    pri_diag += a[i][i]
    sec_diag += a[i][(n-1)-i]

print(abs(pri_diag - sec_diag))