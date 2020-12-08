# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 07:14:08 2020

@author: Nhu Nguyen
"""

"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
"""
import sys

number = input("Input a number: ")

try:
    number = int(number)
    if (number%2 == 0):
        print("Even")
    else:
        print("Odd")
        
except ValueError:
    print("Error: Input is not numeric")

