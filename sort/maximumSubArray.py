#!/usr/bin/env python

def findCross(arr, low, mid, high):
    leftSum = rightSum = 0
    leftMax = arr[mid]
    rightMax = arr[mid + 1]
    left = mid
    right = mid + 1

    for i in xrange(mid, low - 1, -1):
        leftSum += arr[i]
        if leftSum > leftMax:
            leftMax = leftSum
            left = i

    for i in xrange(mid + 1, high + 1):
        rightSum += arr[i]
        if rightSum > rightMax:
            rightMax = rightSum
            right = i
    
    return (left, right, rightMax + leftMax)

def findMaxSubArray(arr, low, high):
    if low == high: return (low, high, arr[low])

    mid = (low + high) / 2
    left_low, left_high, left_sum = findMaxSubArray(arr, low, mid)
    right_low, right_high, right_sum = findMaxSubArray(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = findCross(arr, low, mid, high)

    if left_sum > right_sum and left_sum > cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum > cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)

def main():
    arr = map(int, raw_input('input an array to find maximum subarray: ').split())
    low, high, sum_ = findMaxSubArray(arr, 0, len(arr) - 1)
    print arr[low:high + 1]

if __name__ == '__main__':
    main()


