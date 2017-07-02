#!/usr/bin/env python3.6

def string_unique_chars(s):
    """Determine if a string has all unique characters"""

    try:
        return len(s) == len(set(s))
    except:
        # Generally I think returning bare exceptions probably isn't a good
        # idea. In this case, anything that would cause the above to fail
        # should just mean that it's false (according to the test case in
        # github)
        return False

def is_permutation(str1, str2):
    """Is str1 a permutation of str2"""

    if str1 == None or str2 == None:
        return False

    # naively, converting to set, sorting, and comparing seems to be the
    # best way
    str1 = list(str1)
    str2 = list(str2)

    str1.sort()
    str2.sort()

    return str1 == str2

def is_substring(str1, str2):
    """Return True if str1 is a substring of str2"""
    return str1 in str2

def is_rotation(str1, str2):
    """Test if str1 is a rotation of str2 by calling _is_substring once"""
    if str1 == None or str2 == None:
        return False
    elif len(str1) != len(str2):
        return False

    # Since the strings' lengths are equal, we should be able to add str2
    # to itself and then check if str1 is in str2 + str2.
    return is_substring(str1, str2 + str2)

def compress(s):
    """Return compressed (aaabccdddd = a3bc2d4) string if it saves space"""
    from collections import Counter

    if not s:
        return


    last_char = s[0]
    for i in s:
        if i == last_char:

            pass



