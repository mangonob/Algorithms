#!/usr/bin/env python

def insertSort(arr):
    n = len(arr)
    for i in xrange(1, n):
        t = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > t:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = t

def main():
    numbers = map(int, raw_input('input integer to sort: ').split())
    insertSort(numbers)
    print numbers

if __name__ == '__main__':
    main()
