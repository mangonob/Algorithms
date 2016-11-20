#!/usr/bin/env python

from random import randrange

def randomSample(m, n):
    if m == 0:
        return ()
    else: 
        S = randomSample(m - 1, n - 1)
        i = randrange(1, n + 1)
        if i in S:
            S += n,
        else:
            S += i,
        return S

def randomSample2(m, n):
    S = ()
    for p in xrange(n - m + 1, n + 1):
        i = randrange(1, p + 1)
        if i in S:
            S += p,
        else:
            S += i,
    return S
