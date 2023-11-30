#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = 1
    argv = sys.argv[1:]
    argv_count = len(argv)
    
    if argv_count is 0:
        print("{:d} arguments.".format(argv_count))
    elif argv_count is 1:
        print("{:d} argument:".format(argv_count))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_count))
        while i <= argv_count:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
