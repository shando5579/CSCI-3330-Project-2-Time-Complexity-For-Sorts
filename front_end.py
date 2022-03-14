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

    sys.setrecursionlimit(5000) # Allows us to not overflow stack when calling on recursive functions like quick sort

    # Variables to store average times
    # Bubble
    b_35_n = b_35_o = b_35_r = 0          # Size 35
    b_350_n = b_350_o = b_350_r = 0       # Size 350
    b_3500_n = b_3500_o = b_3500_r = 0    # Size 3500

    # Merge
    m_35_n = m_35_o = m_35_r = 0          # Size 35  
    m_350_n = m_350_o = m_350_r = 0       # Size 350
    m_3500_n = m_3500_o = m_3500_r = 0    # Size 3500

    # Quick
    q_35_b = q_35_m = q_35_r = 0          # Size 35 
    q_350_b = q_350_m = q_350_r = 0       # Size 350
    q_3500_n = q_3500_m = q_3500_r = 0    # Size 3500

    # Selection
    s_35_n = s_35_o = s_35_r = 0          # Size 35
    s_350_n = s_350_o = s_350_r = 0       # Size 350
    s_3500_n = s_3500_o = s_3500_r = 0    # Size 3500

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
        # Bubble sorting with arrays [35]
        # Neutral
        time1 = time.time()
        sortedList = data_generation.neutraldata35_perm.copy()
        sortedList = sorts.bubble_sort(sortedList)
        time1_t = time.time()
        b_35_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = data_generation.ordereddata35_perm.copy()
        sortedList = sorts.bubble_sort(sortedList)
        time2_t = time.time()
        b_35_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = data_generation.reverseddata35_perm.copy()
        sortedList = sorts.bubble_sort(sortedList)
        time3_t = time.time()
        b_35_r += (time3_t - time3)

        # Bubble sorting with arrays [350]
        # Neutral
        time1 = time.time()
        sortedList = data_generation.neutraldata350_perm.copy()
        sortedList = sorts.bubble_sort(sortedList)
        time1_t = time.time()
        b_350_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = data_generation.ordereddata350_perm.copy()
        sortedList = sorts.bubble_sort(sortedList)
        time2_t = time.time()
        b_350_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = data_generation.reverseddata350_perm.copy()
        sortedList = sorts.bubble_sort(sortedList)
        time3_t = time.time()
        b_350_r += (time3_t - time3)

        # Bubble sorting with arrays [3500]
        # Neutral
        time1 = time.time()
        sortedList = data_generation.neutraldata3500_perm.copy()
        sortedList = sorts.bubble_sort(sortedList)
        time1_t = time.time()
        b_3500_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = data_generation.ordereddata3500_perm.copy()
        sortedList = sorts.bubble_sort(sortedList)
        time2_t = time.time()
        b_3500_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = data_generation.reverseddata3500_perm.copy()
        sortedList = sorts.bubble_sort(sortedList)
        time3_t = time.time()
        b_3500_r += (time3_t - time3)

        # Merge sort testing
        # Merge sorting with arrays [35]
        # Neutral
        time1 = time.time()
        sortedList = data_generation.neutraldata35_perm.copy()
        sortedList = sorts.merge_sort(sortedList)
        time1_t = time.time()
        m_35_n += (time1_t - time1)
        
        # Ordered
        time2 = time.time()
        sortedList = data_generation.ordereddata35_perm.copy()
        sortedList = sorts.merge_sort(sortedList)
        time2_t = time.time()
        m_35_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = data_generation.reverseddata35_perm.copy()
        sortedList = sorts.merge_sort(sortedList)
        time3_t = time.time()
        m_35_r += (time3_t - time3)

        # Sorting with arrays [350]
        # Neutral
        time1 = time.time()
        sortedList = data_generation.neutraldata350_perm.copy()
        sortedList = sorts.merge_sort(sortedList)
        time1_t = time.time()
        m_350_n += (time1_t - time1)
        
        # Ordered
        time2 = time.time()
        sortedList = data_generation.ordereddata350_perm.copy()
        sortedList = sorts.merge_sort(sortedList)
        time2_t = time.time()
        m_350_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = data_generation.reverseddata350_perm.copy()
        sortedList = sorts.merge_sort(sortedList)
        time3_t = time.time()
        m_350_r += (time3_t - time3)

        # Sorting with arrays [3500]
        # Neutral
        time1 = time.time()
        sortedList = data_generation.neutraldata3500_perm.copy()
        sortedList = sorts.merge_sort(sortedList)
        time1_t = time.time()
        m_3500_n += (time1_t - time1)
        
        # Ordered
        time2 = time.time()
        sortedList = data_generation.ordereddata3500_perm.copy()
        sortedList = sorts.merge_sort(sortedList)
        time2_t = time.time()
        m_3500_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = data_generation.reverseddata3500_perm.copy()
        sortedList = sorts.merge_sort(sortedList)
        time3_t = time.time()
        m_3500_r += (time3_t - time3)

        # Quick sort testing
        # Quick sorting with arrays [35]
        # Pivot is beginning of list
        time1 = time.time()
        sortedList = data_generation.neutraldata35_perm.copy()
        sorts.quick_sort_b(0, len(sortedList) - 1, sortedList)
        time1_t = time.time()
        q_35_b += (time1_t - time1)

        # Pivot is middle of list
        time1 = time.time()
        sortedList = data_generation.neutraldata35_perm.copy()
        sortedList = sorts.quick_sort_m(sortedList)
        time1_t = time.time()
        q_35_m += (time1_t - time1)

        # Pivot is random
        time1 = time.time()
        sortedList = data_generation.neutraldata35_perm.copy()
        sortedList = sorts.quicksort_r(sortedList, 0, len(sortedList) - 1)
        time1_t = time.time()
        q_35_r += (time1_t - time1)
        
        # Quick sorting with arrays [350]
        # Pivot is beginning of list
        time1 = time.time()
        sortedList = data_generation.neutraldata350_perm.copy()
        sorts.quick_sort_b(0, len(sortedList) - 1, sortedList)
        time1_t = time.time()
        q_350_b += (time1_t - time1)

        # Pivot is middle of list
        time1 = time.time()
        sortedList = data_generation.neutraldata350_perm.copy()
        sortedList = sorts.quick_sort_m(sortedList)
        time1_t = time.time()
        q_350_m += (time1_t - time1)

        # Pivot is random
        time1 = time.time()
        sortedList = data_generation.neutraldata350_perm.copy()
        sortedList = sorts.quicksort_r(sortedList, 0, len(sortedList) - 1)
        time1_t = time.time()
        q_350_r += (time1_t - time1)

        # Quick sorting with arrays [3500]
        # Pivot is beginning of list
        time1 = time.time()
        sortedList = data_generation.neutraldata3500_perm.copy()
        sorts.quick_sort_b(0, len(sortedList) - 1, sortedList)
        time1_t = time.time()
        q_3500_n += (time1_t - time1)

        # Pivot is middle of list
        time1 = time.time()
        sortedList = data_generation.neutraldata3500_perm.copy()
        sortedList = sorts.quick_sort_m(sortedList)
        time1_t = time.time()
        q_3500_m += (time1_t - time1)

        # Pivot is random
        time1 = time.time()
        sortedList = data_generation.neutraldata3500_perm.copy()
        sortedList = sorts.quicksort_r(sortedList, 0, len(sortedList) - 1)
        time1_t = time.time()
        q_3500_r += (time1_t - time1)

        # Selection sort testing
        # Selection sorting with arrays [35]
        # Neutral
        time1 = time.time()
        sortedList = data_generation.neutraldata35_perm.copy()
        sortedList = sorts.selection_sort(sortedList)
        time1_t = time.time()
        s_35_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = data_generation.ordereddata35_perm.copy()
        sortedList = sorts.selection_sort(sortedList)
        time2_t = time.time()
        s_35_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = data_generation.reverseddata35_perm.copy()
        sortedList = sorts.selection_sort(sortedList)
        time3_t = time.time()
        s_35_r += (time3_t - time3)

        # Selection sorting with arrays [350]
        # Neutral
        time1 = time.time()
        sortedList = data_generation.neutraldata350_perm.copy()
        sortedList = sorts.selection_sort(sortedList)
        time1_t = time.time()
        s_350_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = data_generation.ordereddata350_perm.copy()
        sortedList = sorts.selection_sort(sortedList)
        time2_t = time.time()
        s_350_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = data_generation.reverseddata350_perm.copy()
        sortedList = sorts.selection_sort(sortedList)
        time3_t = time.time()
        s_350_r += (time3_t - time3)

        # Selection sorting with arrays [3500]
        # Neutral
        time1 = time.time()
        sortedList = data_generation.neutraldata3500_perm.copy()
        sortedList = sorts.selection_sort(sortedList)
        time1_t = time.time()
        s_3500_n += (time1_t - time1)
    
        # Ordered
        time2 = time.time()
        sortedList = data_generation.ordereddata3500_perm.copy()
        sortedList = sorts.selection_sort(sortedList)
        time2_t = time.time()
        s_3500_o += (time2_t - time2)

        # Reversed
        time3 = time.time()
        sortedList = data_generation.reverseddata3500_perm.copy()
        sortedList = sorts.selection_sort(sortedList)
        time3_t = time.time()
        s_3500_r += (time3_t - time3)

        # Prints newline
        print('Testing complete.\n')

    # Outputting results of testing
    print ('****************************** RESULTS ******************************')

    # Bubble sort results
    print ('\nAverage Bubble Sort results:')

    # Size 35
    print ('- Size 35:')
    print('\t- Neutral: ', (b_35_n / 10))
    print('\t- Ordered: ', (b_35_o / 10))
    print('\t- Reversed: ', (b_35_r / 10))

    # Size 350
    print ('\n- Size 350:')
    print('\t- Neutral: ', round((b_350_n / 10), 8))
    print('\t- Ordered: ', round((b_350_o / 10), 8))
    print('\t- Reversed: ', round((b_350_r / 10), 8))

    # Size 3500
    print ('\n- Size 3500:')
    print('\t- Neutral: ', round((b_3500_n / 10), 8))
    print('\t- Ordered: ', round((b_3500_o / 10), 8))
    print('\t- Reversed: ', round((b_3500_r / 10), 8))

    # Merge sort results
    print ('\nAverage Merge Sort results:')

    # Size 35
    print ('- Size 35:')
    print('\t- Neutral: ', (m_35_n / 10))
    print('\t- Ordered: ', (m_35_o / 10))
    print('\t- Reversed: ', (m_35_r / 10))

    # Size 350
    print ('\n- Size 350:')
    print('\t- Neutral: ', round((m_350_n / 10), 8))
    print('\t- Ordered: ', round((m_350_o / 10), 8))
    print('\t- Reversed: ', round((m_350_r / 10), 8))

    # Size 3500
    print ('\n- Size 3500:')
    print('\t- Neutral: ', round((m_3500_n / 10), 8))
    print('\t- Ordered: ', round((m_3500_o / 10), 8))
    print('\t- Reversed: ', round((m_3500_r / 10), 8))

    # Quick sort results
    print ('\nAverage Quick Sort results:')

    # Size 35
    print ('- Size 35:')
    print('\t- Pivot = Beginning: ', (q_35_b / 10))
    print('\t- Pivot = Middle: ', (q_35_m / 10))
    print('\t- Pivot = Random: ', (q_35_r / 10))

    # Size 350
    print ('\n- Size 350:')
    print('\t- Pivot = Beginning: ', round((q_350_b / 10), 8))
    print('\t- Pivot = Middle: ', round((q_350_m / 10), 8))
    print('\t- Pivot = Random: ', round((q_350_r / 10), 8))

    # Size 3500
    print ('\n- Size 3500:')
    print('\t- Pivot = Beginning: ', round((q_3500_n / 10), 8))
    print('\t- Pivot = Middle: ', round((q_3500_m / 10), 8))
    print('\t- Pivot = Random: ', round((q_3500_r / 10), 8))

    # Selection sort results
    print ('\nAverage Selection Sort results:')

    # Size 35
    print ('- Size 35:')
    print('\t- Neutral: ', (s_35_n / 10))
    print('\t- Ordered: ', (s_35_o / 10))
    print('\t- Reversed: ', (s_35_r / 10))

    # Size 350
    print ('\n- Size 350:')
    print('\t- Neutral: ', round((s_350_n / 10), 8))
    print('\t- Ordered: ', round((s_350_o / 10), 8))
    print('\t- Reversed: ', round((s_350_r / 10), 8))

    # Size 3500
    print ('\n- Size 3500:')
    print('\t- Neutral: ', round((s_3500_n / 10), 8))
    print('\t- Ordered: ', round((s_3500_o / 10), 8))
    print('\t- Reversed: ', round((s_3500_r / 10), 8))


main()