#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

def main():
    if len(sys.argv) != 2:
        return help_me(
            "ERR This takes a single " + 
            "integer as an argument.")
    # need to cast sys.argv[1] as it comes in as a string
    hits = [i for i in range(1, int(sys.argv[1])) 
            if is_multiple(3, i) or 
            is_multiple(5, i)]
    res = 0
    for i in hits:
        res += i
    print(res)
    return 0

def help_me(err=None):
    print(err)

    print("Usage:")
    print(f"\t{sys.argv[0]} integer")
    print(
        "Display sum of multiples of 3 and 5",
        "between 1 to the specified integer."
    )
    return 4

def is_multiple(this, that):
    '''determine if this is a multiple fo that.'''
    status = False
    if that % this == 0:
        status = True
    return status

if __name__ == '__main__':
    sys.exit(main())