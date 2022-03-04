"""
@author: Nickolas Paternoster
@project: Algorithms Project 2
@file: data_generation.py

This file is used to generate different sized arrays
with random integer values to later be sorted with 
various sorting algorithms.

"""

import random

def defaultData():
    'Used for creating array data'

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

    # Chunk that prints arrays
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

