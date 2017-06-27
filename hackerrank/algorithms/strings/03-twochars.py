#!/bin/python3

import sys

def _validate(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False

    return True


#s_len = int(input().strip())
s = input().strip()

# We're going to try brute forcing it first. Get the unique set of characters in
# s by taking the set
s_unique = list(set(s))

max_string_length = 0

# We're basically constructing an matrix of the unique letter combinations and
# iterating over every element in the upper triangle
for i in range(len(s_unique)):
    for j in range(i+1, len(s_unique)):
        if i == j:
            continue

        # we have a unique pair of letters. delete all letters not in this pair
        # and see if we have an alternating string
        new_string = [x for x in s if x in (s_unique[i], s_unique[j])]

        if not _validate(new_string):
            continue

        # We know we have a good string. Is it longer than max_string_length?
        if len(new_string) > max_string_length:
            max_string_length = len(new_string)

print(max_string_length)



