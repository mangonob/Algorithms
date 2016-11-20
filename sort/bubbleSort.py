#!/usr/bin/env python

def bubbleSort(arr):
    n = len(arr)
    for i in xrange(n - 2, -1, -1):
        for j in xrange(0, i + 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = map(int, raw_input('input numbers to sort: ').split())
    bubbleSort(arr)
    print arr

if __name__ == '__main__':
    main()
