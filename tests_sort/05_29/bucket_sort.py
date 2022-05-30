import sort_utils

import math

def insertionSort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        upperIdx = i
        if array[upperIdx] <= array[upperIdx - 1]:
            array[upperIdx], array[upperIdx - 1] = array[upperIdx - 1], array[upperIdx]
            upperIdx -= 1
        else:
            break
    return array

def bucketSort(array):
    if len(array) < 2:
        return array
    nBuckets = len(array)
    maxVal = max(array)
    minVal = min(array)
    valRange = maxVal - minVal
    if valRange == 0:
        return array
    bucketLists = {}
    for i in range(nBuckets):
        bucketLists[i] = []
    # Go through each element.
    for val in array:
        bucket = math.floor(((val - minVal) / valRange) * nBuckets)
        if bucket == nBuckets:
            bucket -= 1
        assert bucket in bucketLists.keys()
        bucketLists[bucket].append(val)
    # Sort each bucket and add to result.
    result = []
    for i in range(nBuckets):
        result += insertionSort(bucketLists[i])
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
