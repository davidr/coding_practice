#!/usr/bin/env python3

def test_0():
    print("Hello, World!")


def test_1(n: int) -> None:
    def _is_even(n: int) -> bool:
        if n % 2 == 0:
            return True
        return False

    if _is_even(n):
        if (n >= 2 and n <= 5) or (n > 20):
            print("Not Weird")
            return
    print("Weird")


def test_2(a: int, b: int) -> None:
    print(a+b)
    print(a-b)
    print(a*b)


def test_3(a: int, b: int) -> None:
    print(a//b)
    print(a/b)


def test_4(n: int) -> None:
    for i in range(n):
        print(i**2)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def print_one_to_n(n: int):
    for i in range(1,n+1):
        print(i, end='')
    print('\n')


if __name__ == "__main__":
    from sys import argv
    try:
        func_args = ", ".join(argv[2:])
    except IndexError:
        func_args = None

    func_to_run = "test_{:d}({:s})".format(int(argv[1]), func_args)
    eval(func_to_run)
