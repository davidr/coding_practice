#!/usr/bin/env python3.7

from importlib import import_module
from timeit import default_timer as timer
from timeit import Timer
import sys
import argparse


def usage(err=None):
    if err:
        print(err, "\n")
    print(f"euler.py ex_number [arg1] [arg2] ... [argn]")
    sys.exit(1)


def main():
    sys.argv.pop(0)
    if len(sys.argv) == 0:
        usage()

    first_arg = sys.argv.pop(0)
    exercise_timer = True if first_arg == '-t' else False

    if exercise_timer:
        ex_no = sys.argv.pop(0)
    else:
        ex_no = first_arg

    if not ex_no.isdigit():
        usage(f"{ex_no} must be numeric")
    ex_no = int(ex_no)

    ex_modulename = f"p{ex_no:03}"
    euler_problem = import_module(ex_modulename)

    # I _think_ that we'll be okay here since I predict all arguments to project euler functions will be integers
    int_args = [int(x) for x in sys.argv]

    start = timer()
    result = euler_problem.compute(*int_args)
    elapsed_time = timer() - start

    if exercise_timer:
        if elapsed_time < 2:
            num_calls = int(2 // elapsed_time)
            start = timer()
            for x in range(0, num_calls):
                euler_problem.compute(*int_args)
            elapsed_time = (timer() - start) / num_calls

    print(f"{result}\t\t(in {elapsed_time:0.3f}s)")


if __name__ == "__main__":
    main()
