#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(argv) - 1))
        i = 0
        for x in range(0, len(argv) - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
            i += 1
