"""
@author: Grant Fugate
@project: Algorithms Project 2
@file: sorts.py

@citation: 

This file is used to impliment all 4 different sorting 
methods which include bubble sort, merge sort, quick sort, 
and selection sort.

"""

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


# Quick Sort
def partition(arr, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if arr[i] <= arr[begin]:
            pivot_idx += 1
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
    arr[pivot_idx], arr[begin] = arr[begin], arr[pivot_idx]
    return pivot_idx

def quick_sort_recursion(arr, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(arr, begin, end)
    quick_sort_recursion(arr, begin, pivot_idx-1)
    quick_sort_recursion(arr, pivot_idx+1, end)

def quick_sort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1
    
    return quick_sort_recursion(arr, begin, end)



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