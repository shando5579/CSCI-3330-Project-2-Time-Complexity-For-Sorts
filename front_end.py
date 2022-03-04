"""
@author: Shandon Probst
@project: Algorithms Project 1
@file: front_end.py

This file is used as the main driver and shows the
measurements of time for algorithms being tested with
randomly generated arrays with sizes in the multiples 
of 10's (array sizes 10, 100, 1000)

"""

import data_generation
import sorts
import time

def main():
    '''Main driver'''

    # Temporary arrays
    test_array1 = []
    test_array2 = []
    test_array3 = []

    # Timers
    time1 = 0
    time1_t = 0
    time1_f = 0

    time2 = 0
    time2_t = 0
    time2_f = 0

    time3 = 0
    time3_t = 0
    time3_f = 0

    # Initializes test arrays
    print('Initializing test arrays.\n')
    data_generation.defaultData()

    # Bubble sort testing
    print('1. Testing bubble sort.')

    # Sorting with arrays [10]
    print('\nSorting arrays with size = 10')
    
    print('\tSorting neutral data...')
    time1 = time.time()
    test_array1 = sorts.bubble_sort(data_generation.neutraldata10_perm)
    time1_t = time.time()
    time1_f = time1_t - time1
    print('\t\tTime taken: ', time1_f)
    
    print('\tSorting ordered data...')
    time2 = time.time()
    test_array2 = sorts.bubble_sort(data_generation.ordereddata10_perm)
    time2_t = time.time()
    time2_f = time2_t - time2
    print('\t\tTime taken: ', time2_f)

    print('\tSorting reversed data...')
    time3 = time.time()
    test_array3 = sorts.bubble_sort(data_generation.reversedata10_perm)
    time3_t = time.time()
    time3_f = time3_t - time3
    print('\t\tTime taken: ', time3_f)

    # Sorting with arrays [100]
    print('\nSorting arrays with size = 100')
    print('\tSorting neutral data...')
    time1 = time.time()
    test_array1 = sorts.bubble_sort(data_generation.neutraldata100_perm)
    time1_t = time.time()
    time1_f = time1_t - time1
    print('\t\tTime taken: ', time1_f)
    
    time2 = time.time()
    print('\tSorting ordered data...')
    test_array2 = sorts.bubble_sort(data_generation.ordereddata100_perm)
    time2_t = time.time()
    time2_f = time2_t - time2
    print('\t\tTime taken: ', time2_f)

    time3 = time.time()
    print('\tSorting reversed data...')
    test_array3 = sorts.bubble_sort(data_generation.reversedata100_perm)
    time3_t = time.time()
    time3_f = time3_t - time3
    print('\t\tTime taken: ', time3_f)

    # Sorting with arrays [1000]
    print('\nSorting arrays with size = 1000')
    print('\tSorting neutral data...')
    time1 = time.time()
    test_array1 = sorts.bubble_sort(data_generation.neutraldata1000_perm)
    time1_t = time.time()
    time1_f = time1_t - time1
    print('\t\tTime taken: ', time1_f)
    
    time2 = time.time()
    print('\tSorting ordered data...')
    test_array2 = sorts.bubble_sort(data_generation.ordereddata1000_perm)
    time2_t = time.time()
    time2_f = time2_t - time2
    print('\t\tTime taken: ', time2_f)

    time3 = time.time()
    print('\tSorting reversed data...')
    test_array3 = sorts.bubble_sort(data_generation.reversedata1000_perm)
    time3_t = time.time()
    time3_f = time3_t - time3
    print('\t\tTime taken: ', time3_f)

main()