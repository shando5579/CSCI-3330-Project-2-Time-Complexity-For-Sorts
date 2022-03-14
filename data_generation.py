"""
@author: Nickolas Paternoster and Shandon Probst
@project: Algorithms Project 2
@file: data_generation.py

This file is used to generate different sized arrays
with random integer values to later be sorted with 
various sorting algorithms.

"""
import random

# Global values for use in other files
global neutraldata35_perm
global neutraldata350_perm
global neutraldata3500_perm
global ordereddata35_perm
global ordereddata350_perm
global ordereddata3500_perm
global reverseddata35_perm
global reverseddata350_perm
global reverseddata3500_perm

def defaultData():
    'Used for creating array data'

    # Random number range
    ranRange = range(1, 10000)

    # Neutral data
    neutraldata35 = random.sample(ranRange, k = 35)
    neutraldata350 = random.sample(ranRange, k = 350)
    neutraldata3500 = random.sample(ranRange, k = 3500)

    # Ordered data
    ordereddata35 = neutraldata35.copy()
    ordereddata35.sort()
    ordereddata350 = neutraldata350.copy()
    ordereddata350.sort()
    ordereddata3500 = neutraldata3500.copy()
    ordereddata3500.sort()

    # Reversed data
    reverseddata35 = ordereddata35.copy()
    reverseddata35.reverse()
    reverseddata350 = ordereddata350.copy()
    reverseddata350.reverse()
    reverseddata3500 = ordereddata3500.copy()
    reverseddata3500.reverse()

    # Global variables defined
    global neutraldata35_perm
    neutraldata35_perm = neutraldata35
    global neutraldata350_perm
    neutraldata350_perm = neutraldata350
    global neutraldata3500_perm
    neutraldata3500_perm = neutraldata3500

    global ordereddata35_perm
    ordereddata35_perm = ordereddata35
    global ordereddata350_perm
    ordereddata350_perm = ordereddata350
    global ordereddata3500_perm
    ordereddata3500_perm = ordereddata3500

    global reverseddata35_perm
    reverseddata35_perm = reverseddata35
    global reverseddata350_perm
    reverseddata350_perm = reverseddata350
    global reverseddata3500_perm
    reverseddata3500_perm = reverseddata3500

'''
    # Chunk that prints arrays
    print("Neutral DATA (35): ", neutraldata35)
    print("\nNeutral DATA (350): ", neutraldata350)
    print("\nNeutral DATA (3500): ", neutraldata3500)

    print("\nORDERED DATA (35): ", ordereddata35)
    print("\nORDERED DATA (350): ", ordereddata350)
    print("\nORDERED DATA (3500): ", ordereddata3500)

    print("\nREVERSED DATA (35): ", reverseddata35)
    print("\nREVERSED DATA (350): ", reverseddata350)
    print("\nREVERSED DATA (3500): ", reverseddata3500)
    
defaultData()
'''