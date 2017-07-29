#!/usr/bin/env python

import re

def find_phone(inputfile):
    with open(inputfile) as f_input:
        for line in f_input:

            area_code = r'\(?(\d{3})\)?'
            exchange  = r'(\d{3})'
            lastnum   = r'(\d{4})'
            connector = r'[ -.]?'
            #phone_regex = r'[(]?([\d]{3})[)]?[.-]?([\d]{3})[.-]?([\d]{4})'
            #phone_regex = r'.*[\d]{3}.*'
            phone_regex = area_code + connector + exchange + \
                    connector + lastnum + r'(?!\d{1})'
            match = re.match('.*' + phone_regex + '.*', line)
            if match:
                print("match!, ({:s}) {:s}-{:s}".format(
                    match.group(1), match.group(2), match.group(3)))


if __name__ == "__main__":
    find_phone('input_small.txt')
