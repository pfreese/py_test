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


print(bucketSort([0, 4, 2, 1, 98, 4, 2, 1, 0]))

rs = [random.uniform(10.5, 75.5) for _ in range(100)]
print(bucketSort(rs))
