#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Calculate the largest prime of an input.
"""

import sys

#primes = [1, 2, 3, 5]

def get_factor(value):  
    prime_state = True
    factor = value
    quotient = None

    for i in range(2, value):
        if value % i == 0:
            prime_state = False
            factor = i
            quotient = int(value / i )
            break
    
    return factor, quotient, prime_state

def main():
    # lazy handling of arguments.
    if len(sys.argv) != 2:
        print("ERR This takes a single integer" +
              " value as an argument")
        return 5

    value = int(sys.argv[1])
    factors = [1]
    prime_state = False

    while not prime_state:
        factor, quotient, prime_state = get_factor(value)
        factors.append(factor)
        value = quotient

    factors.sort()
    print(factors[-1])
    print("all factors: {}".format(factors))
        
    

if __name__ == '__main__':
    sys.exit(main())