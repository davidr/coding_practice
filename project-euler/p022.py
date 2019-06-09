import csv
import eulerlib
from typing import List


def compute() -> int:
    """
    Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it
    into alphabetical order. Then working out the alphabetical value for each name, multiply this
    value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 
    3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 
    938 × 53 = 49714.

    What is the total of all the name scores in the file?

    
    Returns:
        int: [description]
    """
    names = []
    with open("input/p022_names.txt") as f:
	    csv_r = csv.reader(f)
	    for row in csv_r:
		    names += row
    names.sort()

    name_values = []
    for i, name in enumerate(names):
        # names are indexed from 1 for the purposes of calculation, not 0
        order_of_name = i + 1
        name_values.append(order_of_name * sum([eulerlib.ordinal_value_ofletter(a) for a in name]))

    return sum(name_values)