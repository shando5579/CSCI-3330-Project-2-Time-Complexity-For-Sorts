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
import sys

def main():
    '''Main driver'''

    sys.setrecursionlimit(2000) # Allows us to not overflow stack when calling on recursive functions like quick sort

    # Variables to store average times
    # Bubble
    b_10_n = b_10_o = b_10_r = 0          # Size 10
    b_100_n = b_100_o = b_100_r = 0       # Size 100
    b_1000_n = b_1000_o = b_1000_r = 0    # Size 1000

    # Merge
    m_10_n = m_10_o = m_10_r = 0          # Size 10  
    m_100_n = m_100_o = m_100_r = 0       # Size 100
    m_1000_n = m_1000_o = m_1000_r = 0    # Size 1000

    # Quick
    q_10_n = q_10_o = q_10_r = 0          # Size 10 
    q_100_n = q_100_o = q_100_r = 0       # Size 100
    q_1000_n = q_1000_o = q_1000_r = 0    # Size 1000

    # Selection
    s_10_n = s_10_o = s_10_r = 0          # Size 10
    s_100_n = s_100_o = s_100_r = 0       # Size 100
    s_1000_n = s_1000_o = s_1000_r = 0    # Size 1000

    # Runs each test 10 different times and averages the total times for each type of test
    print ('****************************** TESTING ******************************')
    print ('Preparing to run tests 10 different times.\n')
    for i in range(10): 

        # Timers
        time1 = 0
        time1_t = 0

        time2 = 0
        time2_t = 0

        time3 = 0
        time3_t = 0

        # Initializes test arrays
        print('Initializing new test arrays.')
        data_generation.defaultData()

        print ('Running tests...')

        # Bubble sort testing
        # Bubble sorting with arrays [10]
        # Neutral
        time1 = time.time()
        sortedList = sorts.bubble_sort(data_generation.neutraldata10_perm)
        time1_t = time.time()
        b_10_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = sorts.bubble_sort(data_generation.ordereddata10_perm)
        time2_t = time.time()
        b_10_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.bubble_sort(data_generation.reversedata10_perm)
        time3_t = time.time()
        b_10_r += (time3_t - time3)

        # Bubble sorting with arrays [100]
        # Neutral
        time1 = time.time()
        sortedList = sorts.bubble_sort(data_generation.neutraldata100_perm)
        time1_t = time.time()
        b_100_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = sorts.bubble_sort(data_generation.ordereddata100_perm)
        time2_t = time.time()
        b_100_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.bubble_sort(data_generation.reversedata100_perm)
        time3_t = time.time()
        b_100_r += (time3_t - time3)

        # Bubble sorting with arrays [1000]
        # Neutral
        time1 = time.time()
        sortedList = sorts.bubble_sort(data_generation.neutraldata1000_perm)
        time1_t = time.time()
        b_1000_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = sorts.bubble_sort(data_generation.ordereddata1000_perm)
        time2_t = time.time()
        b_1000_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.bubble_sort(data_generation.reversedata1000_perm)
        time3_t = time.time()
        b_1000_r += (time3_t - time3)

        # Merge sort testing
        # Merge sorting with arrays [10]
        # Neutral
        time1 = time.time()
        sortedList = sorts.merge_sort(data_generation.neutraldata10_perm)
        time1_t = time.time()
        m_10_n += (time1_t - time1)
        
        # Ordered
        time2 = time.time()
        sortedList = sorts.merge_sort(data_generation.ordereddata10_perm)
        time2_t = time.time()
        m_10_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.merge_sort(data_generation.reversedata10_perm)
        time3_t = time.time()
        m_10_r += (time3_t - time3)

        # Sorting with arrays [100]
        # Neutral
        time1 = time.time()
        sortedList = sorts.merge_sort(data_generation.neutraldata100_perm)
        time1_t = time.time()
        m_100_n += (time1_t - time1)
        
        # Ordered
        time2 = time.time()
        sortedList = sorts.merge_sort(data_generation.ordereddata100_perm)
        time2_t = time.time()
        m_100_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.merge_sort(data_generation.reversedata100_perm)
        time3_t = time.time()
        m_100_r += (time3_t - time3)

        # Sorting with arrays [1000]
        # Neutral
        time1 = time.time()
        sortedList = sorts.merge_sort(data_generation.neutraldata1000_perm)
        time1_t = time.time()
        m_1000_n += (time1_t - time1)
        
        # Ordered
        time2 = time.time()
        sortedList = sorts.merge_sort(data_generation.ordereddata1000_perm)
        time2_t = time.time()
        m_1000_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.merge_sort(data_generation.reversedata1000_perm)
        time3_t = time.time()
        m_1000_r += (time3_t - time3)

        # Quick sort testing
        # Quick sorting with arrays [10]
        # Neutral
        time1 = time.time()
        sortedList = sorts.quick_sort(0, len(data_generation.neutraldata10_perm) - 1, data_generation.neutraldata10_perm)
        time1_t = time.time()
        q_10_n += (time1_t - time1)
        
        # Ordered
        time2 = time.time()
        sortedList = sorts.quick_sort(0, len(data_generation.ordereddata10_perm) - 1, data_generation.ordereddata10_perm)
        time2_t = time.time()
        q_10_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.quick_sort(0, len(data_generation.reversedata10_perm) - 1, data_generation.reversedata10_perm)
        time3_t = time.time()
        q_10_r += (time3_t - time3)

        
        # Quick sorting with arrays [100]
        # Neutral
        time1 = time.time()
        sortedList = sorts.quick_sort(0, len(data_generation.neutraldata100_perm) - 1, data_generation.neutraldata100_perm)
        time1_t = time.time()
        q_100_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = sorts.quick_sort(0, len(data_generation.ordereddata100_perm) - 1, data_generation.ordereddata100_perm)
        time2_t = time.time()
        q_100_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.quick_sort(0, len(data_generation.reversedata100_perm) - 1, data_generation.reversedata100_perm)
        time3_t = time.time()
        q_100_r += (time3_t - time3)

        # Quick sorting with arrays [1000]
        # Neutral
        time1 = time.time()
        sortedList = sorts.quick_sort(0, len(data_generation.neutraldata1000_perm) - 1, data_generation.neutraldata1000_perm)
        time1_t = time.time()
        q_1000_n += (time1_t - time1)
        
        # Ordered
        time2 = time.time()
        sortedList = sorts.quick_sort(0, len(data_generation.ordereddata1000_perm) - 1, data_generation.ordereddata1000_perm)
        time2_t = time.time()
        q_1000_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.quick_sort(0, len(data_generation.reversedata1000_perm) - 1, data_generation.reversedata1000_perm)
        time3_t = time.time()
        q_1000_r += (time3_t - time3)

        # Selection sort testing
        # Selection sorting with arrays [10]
        # Neutral
        time1 = time.time()
        sortedList = sorts.selection_sort(data_generation.neutraldata10_perm)
        time1_t = time.time()
        s_10_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = sorts.selection_sort(data_generation.ordereddata10_perm)
        time2_t = time.time()
        s_10_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.selection_sort(data_generation.reversedata10_perm)
        time3_t = time.time()
        s_10_r += (time3_t - time3)

        # Selection sorting with arrays [100]
        # Neutral
        time1 = time.time()
        sortedList = sorts.selection_sort(data_generation.neutraldata100_perm)
        time1_t = time.time()
        s_100_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = sorts.selection_sort(data_generation.ordereddata100_perm)
        time2_t = time.time()
        s_100_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.selection_sort(data_generation.reversedata100_perm)
        time3_t = time.time()
        s_100_r += (time3_t - time3)

        # Selection sorting with arrays [1000]
        # Neutral
        time1 = time.time()
        sortedList = sorts.selection_sort(data_generation.neutraldata1000_perm)
        time1_t = time.time()
        s_1000_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = sorts.selection_sort(data_generation.ordereddata1000_perm)
        time2_t = time.time()
        s_1000_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = sorts.selection_sort(data_generation.reversedata1000_perm)
        time3_t = time.time()
        s_1000_r += (time3_t - time3)

        # Prints newline
        print('Testing complete.\n')

    # Outputting results of testing
    print ('****************************** RESULTS ******************************')

    # Bubble sort results
    print ('\nAverage Bubble Sort results:')

    # Size 10
    print ('- Size 10:')
    print('\t- Neutral: ', (b_10_n / 10))
    print('\t- Ordered: ', (b_10_o / 10))
    print('\t- Reversed: ', (b_10_r / 10))

    # Size 100
    print ('\n- Size 100:')
    print('\t- Neutral: ', round((b_100_n / 10), 8))
    print('\t- Ordered: ', round((b_100_o / 10), 8))
    print('\t- Reversed: ', round((b_100_r / 10), 8))

    # Size 1000
    print ('\n- Size 1000:')
    print('\t- Neutral: ', round((b_1000_n / 10), 5))
    print('\t- Ordered: ', round((b_1000_o / 10), 5))
    print('\t- Reversed: ', round((b_1000_r / 10), 5))

    # Merge sort results
    print ('\nAverage Merge Sort results:')

    # Size 10
    print ('- Size 10:')
    print('\t- Neutral: ', (m_10_n / 10))
    print('\t- Ordered: ', (m_10_o / 10))
    print('\t- Reversed: ', (m_10_r / 10))

    # Size 100
    print ('\n- Size 100:')
    print('\t- Neutral: ', round((m_100_n / 10), 8))
    print('\t- Ordered: ', round((m_100_o / 10), 8))
    print('\t- Reversed: ', round((m_100_r / 10), 8))

    # Size 1000
    print ('\n- Size 1000:')
    print('\t- Neutral: ', round((m_1000_n / 10), 5))
    print('\t- Ordered: ', round((m_1000_o / 10), 5))
    print('\t- Reversed: ', round((m_1000_r / 10), 5))

    # Quick sort results
    print ('\nAverage Quick Sort results:')

    # Size 10
    print ('- Size 10:')
    print('\t- Neutral: ', (q_10_n / 10))
    print('\t- Ordered: ', (q_10_o / 10))
    print('\t- Reversed: ', (q_10_r / 10))

    # Size 100
    print ('\n- Size 100:')
    print('\t- Neutral: ', round((q_100_n / 10), 8))
    print('\t- Ordered: ', round((q_100_o / 10), 8))
    print('\t- Reversed: ', round((q_100_r / 10), 8))

    # Size 1000
    print ('\n- Size 1000:')
    print('\t- Neutral: ', round((q_1000_n / 10), 5))
    print('\t- Ordered: ', round((q_1000_o / 10), 5))
    print('\t- Reversed: ', round((q_1000_r / 10), 5))

    # Selection sort results
    print ('\nAverage Selection Sort results:')

    # Size 10
    print ('- Size 10:')
    print('\t- Neutral: ', (s_10_n / 10))
    print('\t- Ordered: ', (s_10_o / 10))
    print('\t- Reversed: ', (s_10_r / 10))

    # Size 100
    print ('\n- Size 100:')
    print('\t- Neutral: ', round((s_100_n / 10), 8))
    print('\t- Ordered: ', round((s_100_o / 10), 8))
    print('\t- Reversed: ', round((s_100_r / 10), 8))

    # Size 1000
    print ('\n- Size 1000:')
    print('\t- Neutral: ', round((s_1000_n / 10), 5))
    print('\t- Ordered: ', round((s_1000_o / 10), 5))
    print('\t- Reversed: ', round((s_1000_r / 10), 5))


main()