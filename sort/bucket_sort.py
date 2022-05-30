import sort_utils

import math
import random

def insertionSort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        while i >= 1:
            if array[i-1] > array[i]:
                array[i], array[i-1] = array[i-1], array[i]
            else:
                break
            i -= 1
    return array

def bucketSort(array):
    if len(array) < 2:
        return array
    buckets = {}
    max_val = max(array)
    min_val = min(array)
    valRange = max_val - min_val
    nBuckets = len(array)
    for i in range(nBuckets):
        buckets[i] = []
    for val in array:
        bucket = round(((val - min_val) / valRange) * nBuckets)
        if bucket == nBuckets:
            bucket -= 1
        assert bucket in buckets.keys(), f"Want bucket {bucket} out of {nBuckets} buckets, val ={val}"
        buckets[bucket].append(val)

    result = []
    for i in range(nBuckets):
        result += insertionSort(buckets[i])
    return result

# TESTS

intsActual = bucketSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = bucketSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert bucketSort([]) == []
assert bucketSort([2]) == [2]
