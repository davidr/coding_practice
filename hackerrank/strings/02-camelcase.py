#!/usr/bin/python3

"""
Alice wrote a sequence of words in CamelCase as a string of letters, s, having
the following properties:

 * It is a concatenation of one or more words consisting of English letters.
 * All letters in the first word are lowercase.
 * For each of the subsequent words, the first letter is uppercase and rest of
   the letters are lowercase.

Given s, print the number of words in s on a new line.
"""

s = input().strip()
s = list(s)

# We know that the first word starts at s[0], so we can just start at s[1]
wordcount = 1
i = 1

while i < len(s):
    if s[i].isupper():
        # Insert a newline into s and then bump the index to account for the added
        # element
        wordcount += 1

    i += 1

print(wordcount)
