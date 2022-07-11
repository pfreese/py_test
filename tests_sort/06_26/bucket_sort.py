import sort_utils

def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]


def insertion_sort(array):
    n = len(array)
    if n < 2:
        return array

    for start_idx in range(1, n):
        for i in range(start_idx, 0, -1):
            if array[i-1] >= array[i]:
                swap(array, i-1, i)
            else:
                break
    return array


def bucketSort(array):
    n = len(array)
    if n < 2:
        return array

    min_val = min(array)
    max_val = max(array)

    val_range = max_val - min_val
    if val_range == 0:
        return array

    bucket_vals = {}
    for bucket in range(n):
        bucket_vals[bucket] = []

    # Go through each value.
    for val in array:
        bucket = int(((val - min_val) / val_range) * n)
        if bucket == n:
            bucket -= 1
        bucket_vals[bucket].append(val)

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
