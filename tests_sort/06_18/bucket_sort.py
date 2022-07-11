import sort_utils

def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]


def insertion_sort(array):
    n = len(array)
    if n < 2:
        return array
    for i in range(1, n):
        j = i
        while j > 0:
            if array[j - 1] <= array[j]:
                swap(array, j, j - 1)
            j -= 1
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

    bucket_lists = {}
    bucket_idxs = list(range(n))
    for i in bucket_idxs:
        bucket_lists[i] = []

    for val in array:
        idx = int(((val - min_val) / range_vals) * n)
        if idx == n:
            idx -= 1
        assert idx in bucket_idxs
        bucket_lists[idx].append(val)

    result = []
    for i in bucket_idxs:
        result += insertion_sort(bucket_lists[i])

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
