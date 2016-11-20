#!/usr/bin/env python

import copy
def merge(arr, start, mid, end):
    '''
    merge two sorted parts of array
    '''
    n1 = mid - start + 1
    n2 = end - mid
    L = arr[start: mid + 1]
    L.append(float('inf'))
    R = arr[mid + 1: end + 1]
    R.append(float('inf'))
    i = 0
    j = 0
    for k in xrange(start, end + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def mergeSort(arr, start, end):
    if start >= end: return
    mid = (start + end) / 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end)
    merge(arr, start, mid, end)

def sort(arr):
    mergeSort(arr, 0, len(arr) - 1)

def main():
    arr = map(int, raw_input('input numbers to merge sort: ').split())
    sort(arr)
    print arr

if __name__ == '__main__':
    main()

