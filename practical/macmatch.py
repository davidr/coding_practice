#!/usr/bin/env python3

import re

def main():
    with open("input_small.txt") as f_input:
        for line in f_input:

            print(line, end='')
            hex_chars = "0-9a-fA-F"

            re_string = r'([a-fA-F0-9]{2}[:|\-]?){6}'
            re_string = "([0-9a-fA-F]{2}[:]){5}"

            # match = re.search(r"([hex_chars]{2}[\-:]){2}", line)
            match = re.search(re_string, line)
            if match:
                print(f"woot {match.group()}")




if __name__ == "__main__":
    main()
