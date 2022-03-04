"""
@author: Nickolas Paternoster
@project: Algorithms Project 2
@file: data_generation.py

This file is used to generate different sized arrays
with random integer values to later be sorted with 
various sorting algorithms.

"""

import random

# Global values for use in other files
global neutraldata10_perm
global neutraldata100_perm
global neutraldata1000_perm
global ordereddata10_perm
global ordereddata100_perm
global ordereddata1000_perm
global reversedata10_perm
global reversedata100_perm
global reversedata1000_perm

def defaultData():
    'Used for creating array data'

    # Random number range
    ranRange = range(1, 1000)

    # Neutral data
    neutraldata10 = random.choices(ranRange, k = 11)
    neutraldata100 = random.choices(ranRange, k = 101)
    neutraldata1000 = random.choices(ranRange, k = 1001)

    # Ordered data
    ordereddata10 = list(range(1, 11))
    ordereddata100 = list(range(1, 101))
    ordereddata1000 = list(range(1, 1001))

    # Reversed data
    reversedata10 = list(range(1, 11))
    reversedata10.reverse()

    reversedata100 = list(range(1, 101))
    reversedata100.reverse()

    reversedata1000 = list(range(1, 1001))
    reversedata1000.reverse()

    # Global variables defined
    global neutraldata10_perm
    neutraldata10_perm = neutraldata10
    global neutraldata100_perm
    neutraldata100_perm = neutraldata100
    global neutraldata1000_perm
    neutraldata1000_perm = neutraldata1000

    global ordereddata10_perm
    ordereddata10_perm = ordereddata10
    global ordereddata100_perm
    ordereddata100_perm = ordereddata100
    global ordereddata1000_perm
    ordereddata1000_perm = ordereddata1000

    global reversedata10_perm
    reversedata10_perm = reversedata10
    global reversedata100_perm
    reversedata100_perm = reversedata100
    global reversedata1000_perm
    reversedata1000_perm = reversedata1000

'''    # Chunk that prints arrays
    print("Neutral DATA (10): ", neutraldata10)
    print("\nNeutral DATA (100): ", neutraldata100)
    print("\nNeutral DATA (1000): ", neutraldata1000)

    print("\nORDERED DATA (10): ", ordereddata10)
    print("\nORDERED DATA (100): ", ordereddata100)
    print("\nORDERED DATA (1000): ", ordereddata1000)

    print("\nREVERSED DATA (10): ", reversedata10)
    print("\nREVERSED DATA (100): ", reversedata100)
    print("\nREVERSED DATA (1000): ", reversedata1000)

    
defaultData()
'''