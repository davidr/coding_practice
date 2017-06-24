#!/bin/python3

import sys
from collections import Counter


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

counts = Counter()

# Iterate through the array, counting elements <, =, and > 0
for i in arr:
    if i < 0:
        counts['neg'] += 1
    elif i == 0:
        counts['zed'] += 1
    else:
        counts['pos'] += 1

for count in ('pos', 'neg', 'zed'):
    print(counts[count] / n)
