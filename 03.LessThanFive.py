# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:06:22 2020

@author: Nhu Nguyen
"""
"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.
"""


"""
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Extras:
    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""
# This function returns all values that are less than 5
def lst_less_than_5(lst, number):
    return [item for item in lst if item <number]
    
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = input("Please enter a number: ")
try:
    number = int(number)
    newlist = lst_less_than_5(lst, number)
    
    print(*newlist, sep=', ')
except ValueError:
    print("The value entered is not numeric.")

    











