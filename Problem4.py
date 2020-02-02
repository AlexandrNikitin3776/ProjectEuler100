# -*- coding: utf-8 -*-
"""
Project Euler. Problem 4. Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def ispalindrome(n):
    '''
        returns is number n palindrome or not
    '''
    return str(n) == str(n)[::-1]
    
def largestpalindrome():
    '''
        returns the largest palindrome made from the product of two 3-digit numbers
    '''
    maxpalindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, i, -1):
            product = i * j
            if product < maxpalindrome:
                break
            if ispalindrome(product) and product > maxpalindrome:
                maxpalindrome = product
    return maxpalindrome

print(largestpalindrome())