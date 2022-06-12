import sort_utils

import math


def insertionSort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        j = i
        while j > 0:
            if array[j] <= array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1
            else:
                break
    return array


def bucketSort(array):
    nBuckets = len(array)
    if nBuckets < 2:
        return array
    maxVal = max(array)
    minVal = min(array)
    valRange = maxVal - minVal
    if valRange == 0:
        return array
    bucketIdxs = list(range(nBuckets))

    bucketVals = {}
    for i in range(nBuckets):
        bucketVals[i] = []

    for val in array:
        bucketIdx = math.floor((val - minVal) * nBuckets / valRange)
        if bucketIdx == nBuckets:
            bucketIdx -= 1
        assert bucketIdx in bucketIdxs
        bucketVals[bucketIdx].append(val)

    #
    result = []
    for i in range(nBuckets):
        result += insertionSort(bucketVals[i])
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
