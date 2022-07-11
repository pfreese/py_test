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
            if array[j-1] >= array[j]:
                swap(array, j-1, j)
                j -= 1
            else:
                break
    return array

def bucket_sort(array):
    n = len(array)
    if n < 2:
        return array

    min_val = min(array)
    max_val = max(array)
    val_range = max_val - min_val
    if val_range == 0:
        return array

    bucket_lists = {}
    for i in range(n):
        bucket_lists[i] = []

    for val in array:
        bucket_idx = int(((val - min_val) / val_range) * n)
        if bucket_idx == n:
            bucket_idx -= 1
        bucket_lists[bucket_idx].append(val)

    result = []
    for i in range(n):
        result += insertion_sort(bucket_lists[i])
    return result


# TESTS

intsActual = bucket_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = bucket_sort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert bucket_sort([]) == []
assert bucket_sort([2]) == [2]
