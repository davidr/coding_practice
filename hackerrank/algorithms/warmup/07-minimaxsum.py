#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

# We want the min sum and the maxsum. Some notes:
#  - minsum is sum(arr) - max(arr)
#  - maxsum is sum(arr) - min(arr)
#
# min/max(arr) is O(n), so don't use sort. summing and then min and max would be 3x
# through if we did that, so we should sum and track min/max at the same time.
#
# Questions:
#  - is that really faster?

if len(arr) == 0:
    return None

# Start somewhere to avoid type errors, so let min = max = arr[0]
min_arr = arr[0]
max_arr = arr[0]
sum_arr = 0

for element in arr:
    if element < min_arr:
        min_arr = element
    if element > max_arr:
        max_arr = element

    sum_arr += element

print(sum_arr - max_arr, sum_arr - min_arr)
