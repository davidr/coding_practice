#!/bin/python3

import sys

def super_reduced_string(s):
    # Complete this function
    """
    Steve has a string, s, consisting of n lowercase English alphabetic
    letters. In one operation, he can delete any pair of adjacent letters
    with same value. For example, string "aabcc" would become either "aab"
    or "bcc" after  operation.

    Steve wants to reduce s as much as possible. To do this, he will repeat
    the above operation as many times as it can be performed. Help Steve
    out by finding and printing s's non-reducible form!

    if the final string is empty print "Empty String" otherwise, print the
    final nonreducible string
    """
    s = list(s)

    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            del s[i:i+2]

            # If we're not at the beginning of the string, we need to back the
            # index up to see if we've created a new adjacency
            if i > 0:
                i -= 1
        else:
            i += 1

    if len(s) == 0:
        return "Empty String"

    return "".join(s)


s = input().strip()
result = super_reduced_string(s)
print(result)

