# -*- coding: utf-8 -*-
"""
Project Euler. Problem 1.
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def arSum(start, stop, n):
    '''
        Returns sum of arithmetic progression where:
            start - the first element;
            stop - the last element;
            n - the common difference between terms.
    '''
    return (start + stop) * n // 2

def sumbase(base, finish):
    '''
        Returns sum of numbers below number finish that are multiples of base.
    '''
    stop = ((finish - 1)// base) * base
    n = stop // base + 1
    return arSum(0, stop, n)

n = int(input('Could you please write a number the sum below should be calculated: '))
print(sumbase(3, n) + sumbase(5, n) - sumbase(15, n))