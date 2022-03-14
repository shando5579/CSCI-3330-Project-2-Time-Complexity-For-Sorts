"""
@author: Grant Fugate
@project: Algorithms Project 2
@file: sorts.py

@Citations: 
    Quick Sort Algorithm - medium.com
    (https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889)
    
    Bubble Sort Algorithm - medium.com
    (https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889)
    
    Merge Sort Algorithm (Beginning Element Pivot) - geeksforgeeks.org
    (https://www.geeksforgeeks.org/merge-sort/)

    Merge Sort Algorithm (Middle Element Pivot) - gist.github.com
    (https://gist.github.com/dtaivpp/1e23ebcb1e654a5a6fef2bcce79deb53)

    Merge Sort Algorithm (Random Element Pivot) - geeksforgeeks.org
    (https://www.geeksforgeeks.org/quicksort-using-random-pivoting/)
    
    Selection Sort Algorithm - medium.com
    (https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889)

This file is used to impliment all 4 different sorting 
methods which include bubble sort, merge sort, quick sort, 
and selection sort.

"""

import random

# Bubble Sort
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr

# Merge Sort
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

# Quick Sort with index = 0 element
def partition_b(start, end, array):
     
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
     
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
         
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
             
        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1
         
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
     
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    # Returning end pointer to divide the array into 2
    return end
     
# The main function that implements QuickSort
def quick_sort_b(start, end, array):
     
    if (start < end):
         
        # p is partitioning index, array[p]
        # is at right place
        p = partition_b(start, end, array)
         
        # Sort elements before partition
        # and after partition
        quick_sort_b(start, p - 1, array)
        quick_sort_b(p + 1, end, array)

# Quick Sort with index = middle
def partition_m(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort_m(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition_m(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

def quicksort_r(arr, start , stop):
    '''The function which implements QuickSort.
    arr :- array to be sorted.
    start :- starting index of the array.
    stop :- ending index of the array.'''
    if(start < stop):
         
        # pivotindex is the index where
        # the pivot lies in the array
        pivotindex = partitionrand(arr,\
                             start, stop)
         
        # At this stage the array is
        # partially sorted around the pivot.
        # Separately sorting the
        # left half of the array and the
        # right half of the array.
        quicksort_r(arr , start , pivotindex-1)
        quicksort_r(arr, pivotindex + 1, stop)
 
# This function generates random pivot,
# swaps the first element with the pivot
# and calls the partition function.
def partitionrand(arr , start, stop):
 
    # Generating a random number between the
    # starting index of the array and the
    # ending index of the array.
    randpivot = random.randrange(start, stop)
 
    # Swapping the starting element of
    # the array and the pivot
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition_r(arr, start, stop)
 

def partition_r(arr,start,stop):
    '''This function takes the first element as pivot,
    places the pivot element at the correct position
    in the sorted array. All the elements are re-arranged
    according to the pivot, the elements smaller than the
    pivot is places on the left and the elements
    greater than the pivot is placed to the right of pivot.'''
    pivot = start # pivot
     
    # a variable to memorize where the
    i = start + 1
     
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
         
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)

# Selection Sort
def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr