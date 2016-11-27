#!/usr/bin/env python


def parent(i):
    return (i - 1) / 2

def left(i):
    return (2 * i) + 1

def right(i):
    return 2 * (i + 1)

class heap(list):
    heap_size = 0

def max_heapify(A, i):
    l = left(i)
    r = right(i)
    largest = max([x for x in [i, l, r] if x < A.heap_size], key = lambda x: A[x])
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_heap(A):
    A = heap(A)
    A.heap_size = len(A)

    for i in xrange(len(A) / 2, -1, -1):
        max_heapify(A, i)

    return A

def heapSort(A):
    A = build_heap(A)
    for i in xrange(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A.heap_size -= 1
        max_heapify(A, 0)
    return A
