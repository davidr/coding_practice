def swap_case(s):
    s = list(s)
    for i, char in enumerate(s):
        if char.isupper():
            s[i] = char.lower()
        if char.islower():
            s[i] = char.upper()
    return "".join(s)

def split_and_join(line):
    return "-".join(line.split(" "))

def print_full_name(a, b):
    print('Hello {} {}! You just delved into python.'.format(a, b))

def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return "".join(string)

def count_substring(string, sub_string):
    count = 0
    substr_len = len(sub_string)
    for i in range(0, len(string)):
        if string[i:i + substr_len] == sub_string:
            count += 1
    return count

def validate_string(s):
    print(any([char.isalnum() for char in s]))
    print(any([char.isalpha() for char in s]))
    print(any([char.isdigit() for char in s]))
    print(any([char.islower() for char in s]))
    print(any([char.isupper() for char in s]))

def capitalize(string):
    s = string.split(" ")
    for i, word in enumerate(s):
        s[i] = word.capitalize()

    return " ".join(s)

