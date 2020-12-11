# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 07:33:28 2020

@author: QuynhNhu
"""
import random

list1 = random.sample(range(1, 100), random.randint(1, 20))
list2 = random.sample(range(1, 100), random.randint(1, 20))
newlst = []

print("List 1: ", list1)
print("List 2: ", list2)

newlst = [e1 for e1 in list1 if (e1 not in newlst) & (e1 in list2)]
        
print(*newlst)