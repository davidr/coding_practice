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
    def _format_compress(char, count):
        string = char
        if count > 1:
            string += '{:d}'.format(count)

        return string

    if not s:
        return


    # set initial state
    char_count = 0
    last_char = s[0]
    s_compress = ''

    for char in s:
        if char == last_char:
            # More of the same character. Increment counter and move on.
            char_count += 1
        else:
            # new_character
            s_compress += _format_compress(last_char, char_count)
            last_char = char
            char_count = 1

    # Take care of whatever string is last
    s_compress += _format_compress(last_char, char_count)

    if len(s_compress) < len(s):
        return s_compress
    else:
        return "".join(s)

def reverse(s):
    """Reverse chars in place, i.e. not cheating and using s[::-1]"""

    s = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return "".join(s)

def find_diff(s, t):
    """Find the character in t that is not in s"""
    s = set(s)
    t = set(t)

    return list(set.difference(t, s))[0]

def two_sum(nums, val):
    """Find the indices of nums for two numbers that sum to val. There will always
    be exactly one solution."""

    # We could make a matrix of the combinations of elements, and then traverse
    # the upper triangle, but that's slow. If we just run through the list, store
    # val - nums[i] in a hash table, and then look up each new integer in the hash
    # table, etc. we should be okay

    seen_complements = {}

    for i, num in enumerate(nums):
        complement = val - num

        if num in seen_complements:
            return [seen_complements[num], i]

        else:
            seen_complements[complement] = i

def fizzbuzz(num):
    if type(num) != int or num < 1:
        raise Exception

    print_newline = False
    for i in range(1, num +1):
        print(i)
        if i % 3 == 0:
            print('Fizz', end='')
            print_newline = True
        if i % 5 == 0:
            print('Buzz', end='')
            print_newline = True

        if print_newline:
            print('')
        print_newline = False





