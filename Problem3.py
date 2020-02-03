# -*- coding: utf-8 -*-
"""
Project Euler. Problem 3. Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
def largestprimefactor(n):
    n = abs(n)
    if n <= 3:
        return n
    maxfactor = 1
    if n % 2 == 0:
        maxfactor = 2
        while n % 2 == 0:
            n = n // 2
    i = 3
    while i <= n:
        if n % i == 0:
            maxfactor = i
            n = n // i
        else:
            i += 2
    return maxfactor


n = int(input('Could you please write a number the largest prime factor of should be calculated: '))
print(largestprimefactor(n))
