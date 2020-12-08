# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 05:56:58 2020

@author: Nhu Nguyen
"""

"""
    Create a program that asks the user to enter their name and their age. 
    Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

import datetime

name = input("Input your name: ")
print("Your name is ", name)

try:
    # In case the value inputted for age or additional is not number
    age = input("Input your age: ")
    print("Your age is ", age)
    age = int(age)
    
    if (age < 0):
        print("Age can't be negative, try again")
    else:
        times = input("Please enter an additional number: ")
        times = int(times)
        
        
        # Get the current year
        now = datetime.datetime.now()
        currentyear = now.year
        
        if (age >= 100):
            print(('You turned 100 in ' + str(currentyear - age + 100) + '\n') * times)
        else:
            print(('You will reach 100 at ' + str(currentyear + 100 - age) + '\n') * times)
    
    
except ValueError:
    print("Error: Age or additional number must be numeric.")
    


