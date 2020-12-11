# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 18:24:25 2020

@author: QuynhNhu

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

"""

def list_of_divisors(number):
    return [element for element in range(2, number) if (number % element == 0)]
    
number = input("Input a number: ")

try:
    # convert the input value to integer
    number = int(number)
        
    lst = list_of_divisors(number)
    print(*lst)

except ValueError:
    print("Input data must be numeric.")