#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    # x = Cat A
    # y = Cat B
    # z = Mouse
    loc = {
        'Cat A' : x,
        'Cat B' : y,
        'Mouse C': z,
    }

    # If the cats start at the same place, the mouse wins
    if loc['Cat A'] == loc['Cat B']:
        print("Mouse C")
        continue

    # which cat is closer to zero?
    if loc['Cat A'] < loc['Cat B']:
        left_cat  = 'Cat A'
        right_cat = 'Cat B'
    else:
        left_cat  = 'Cat B'
        right_cat = 'Cat A'

    # The mouse is not between the two cats, so whichever cat he's closest to wins
    if loc['Mouse C'] <= loc[left_cat]:
        print(left_cat)
    elif loc['Mouse C'] >= loc[right_cat]:
        print(right_cat)
    else:
        left_cat_tomouse  = abs(loc['Mouse C'] - loc[left_cat])
        right_cat_tomouse = abs(loc['Mouse C'] - loc[right_cat])

        if left_cat_tomouse == right_cat_tomouse:
            print("Mouse C")
        elif left_cat_tomouse < right_cat_tomouse:
            print(left_cat)
        elif left_cat_tomouse > right_cat_tomouse:
            print(right_cat)
