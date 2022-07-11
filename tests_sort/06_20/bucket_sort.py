import sort_utils

def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]

def insertion_sort(array):
    n = len(array)
    if n < 2:
        return array
    for i in range(1, n):
        j = i
        while j >= 1:
            if array[j] <= array[j-1]:
                swap(array, j, j-1)
                j -= 1
            else:
                break
    return array


def bucketSort(array):
    n = len(array)
    if n < 2:
        return array

    min_val = min(array)
    max_val = max(array)
    range_vals = max_val - min_val
    if range_vals == 0:
        return array

    # n buckets.
    bucket_vals = {}
    for bucket in range(n):
        bucket_vals[bucket] = []

    for val in array:
        bucket = int(((val - min_val) / range_vals) * n)
        if bucket == n:
            bucket -= 1
        bucket_vals[bucket].append(val)

    # Add sorted buckets to final result.
    result = []
    for bucket in range(n):
        result += insertion_sort(bucket_vals[bucket])
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
