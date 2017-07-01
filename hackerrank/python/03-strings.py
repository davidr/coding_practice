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

#def count_substring(string, sub_string):
#    return
