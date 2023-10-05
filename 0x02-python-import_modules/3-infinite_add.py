#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    if len(argv) == 1:
        print("{}".format(sum))
    else:
        i = 0
        for x in range(0, len(argv) - 1):
            sum += int(argv[i + 1])
            i += 1
        print(sum)
