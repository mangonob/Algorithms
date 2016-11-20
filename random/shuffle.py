#!/usr/bin/env python

from random import randrange

def shuffle(A):
    n = len(A)
    for i in xrange(0, n):
        r = randrange(i, n)
        A[i], A[r] = A[r], A[i]
