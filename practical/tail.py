#!/usr/bin/env python3

import os
import sys

FILENAME="input.txt"
TAIL_LINES=10

def main():
    if not os.path.exists(FILENAME):
        print(f'{FILENAME} does not exist')
        sys.exit(1)

    wholefile_tail(FILENAME, TAIL_LINES)
    print()
    wholefile_list_tail(FILENAME, TAIL_LINES)
    print()
    byline_runningbuffer_tail(FILENAME, TAIL_LINES)


def wholefile_tail(filename, lines):
    with open(filename, 'r') as f_input:
        contents = f_input.read()
        contents = contents.split('\n')

        if len(contents) <= lines:
            print("\n".join(contents), end="")
        else:
            print("\n".join(contents[-(lines+1):]), end="")

def wholefile_list_tail(filename, lines):
    with open(filename, 'r') as f_input:
        contents = list(f_input)

        if len(contents) <= lines:
            print("".join(contents), end="")
        else:
            print("".join(contents[-(lines):]), end="")


def byline_runningbuffer_tail(filename, lines):
    with open(filename, 'r') as f_input:
        n_lines = sum([1 for line in f_input])

        # We've counted the number of lines in the file, so we need to just start
        # over and skip to the correct line
        f_input.seek(0)

        line_no = 1
        while line_no < n_lines - (lines + 1):
            next(f_input)
            line_no += 1

        # We're at the correct place, just print the rest of the lines
        for line in f_input:
            print(line, end="")


def fromend_tail(filename, lines):
    bufsize = 100

    tailbuf = ''

    with open(filename, 'r') as f_input:
        # Seek to end of file
        f_input.seek(0, 2)

        num_lines_inbuf = 0
        while f_input.tell() - bufsize > 0:

            # back the pointer up by 100 and read 100
            f_input.seek(f_input.tell() - bufsize)
            readbuf = f_input.read(bufsize)

            i = len(readbuf) - 1
            while i >= 0:
                if readbuf[i] == '\n':
                    print("line!, {:d}".format(i))
                    num_lines_inbuf += 1

                    if num_lines_inbuf == lines:
                        # We've got all we need!
                        tailbuf = readbuf[i+1:] + tailbuf
                        break

                i -= 1

            if num_lines_inbuf == lines:
                break

            # We've reached the beginning of the buffer and haven't seen enough
            # newlines yet
            tailbuf = readbuf + tailbuf

            # Seek back
            f_input.seek(f_input.tell() - bufsize)

        print("S")
        print(tailbuf, end='')
        print("E")






if __name__ == "__main__":
    main()
