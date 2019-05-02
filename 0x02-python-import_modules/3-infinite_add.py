#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    totalen = len(sys.argv)
    totalarg = 0
    for i in range(1, totalen):
        totalarg = totalarg + int(sys.argv[i])
    print(totalarg)
