#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

'''
Calculate the Fibonacci sequence until provided value.
Take even values in the sequence between 1 and that value
and sum only the even values.
'''

def fibonacci_get_next(x,y):
    '''calculate the next two values.'''
    nx = x + y
    ny = y + nx
    return nx,ny

def print_help(msg=None):
    '''Pretty help in a lazy-argument-handling world.'''
    if msg:
        print(msg)
 
    print("Usage:")
    print("\t{} integer [debug]".format(sys.argv[0]))
    print("\nSum even values in the Fibonacci sequence"+
             " from 1 to provided upper bound.")

def main():
    # if they want help, do nothing else.
    if 'help' in sys.argv:
        print_help()
        return 1

    x = 1
    y = 2
    debug = False
    evens = []

    # lazy command line argument handling,
    while 'debug' in sys.argv:
        sys.argv.remove('debug')
        debug = True

    if len(sys.argv) == 1:
        print_help("ERR You need to provide an integer to use as" + 
                   " the upper bound!")
        return 5

    # main logic.
    while y < int(sys.argv[1]):
        for i in x,y:
            if i % 2 == 0:
                evens.append(i)
        x, y = fibonacci_get_next(x,y) 

    # provide output.
    if debug:
        print('DEBUG calculated the following list '+
              'of even values: {}'.format(evens))

    print('Result: {}'.format(sum(evens)))

if __name__ == '__main__':
    sys.exit(main())
