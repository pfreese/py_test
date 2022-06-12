import sort_utils

import math

# Sort into n buckets.
# Do insertion sort on each bucket.

def insertion_sort(array):
    n = len(array)
    if n < 2:
        return array
    for i in range(1, n):
        j = i
        while j > 0:
            if array[j-1] >= array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1
            else:
                break
    return array


def get_bucket(val, min_val, val_range, n):
    bucket = math.floor(((val - min_val) / val_range) * n)
    if bucket == n:
        bucket -= 1
    assert bucket < n
    assert bucket >= 0
    return bucket


def bucketSort(array):
    n = len(array)
    if n < 2:
        return array
    min_val = min(array)
    max_val = max(array)
    val_range = max_val - min_val
    if val_range == 0:
        return array

    # Make buckets.
    bucket_lists = {}
    bucket_idxs = list(range(n))
    for idx in bucket_idxs:
        bucket_lists[idx] = []

    # Go through each value and assign it to its bucket.
    for val in array:
        idx = get_bucket(val, min_val, val_range, n)
        bucket_lists[idx].append(val)

    # Sort within each bucket with insertion sort.
    result = []
    for idx in bucket_idxs:
        result += insertion_sort(bucket_lists[idx])
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
