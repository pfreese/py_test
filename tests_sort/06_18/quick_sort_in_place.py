import sort_utils

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return

def partition(array, lower, upper):
    assert lower < upper
    pivot_val = array[lower]

    i = lower + 1
    j = lower + 1
    while j <= upper:
        if array[j] <= pivot_val:
            swap(array, j, i)
            i += 1
        j += 1
    # Swap pivot_val.
    pivot_idx = i - 1
    swap(array, lower, pivot_idx)
    return pivot_idx


def quicksort_helper(array, lower, upper):
    if upper <= lower:
        return
    pivot_idx = partition(array, lower, upper)
    quicksort_helper(array, lower, pivot_idx - 1)
    quicksort_helper(array, pivot_idx + 1, upper)
    return


def quickSort(array):
    n = len(array)
    if n < 2:
        return array
    quicksort_helper(array, 0, len(array) - 1)
    return array



# TESTS

intsActual = quickSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quickSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quickSort([]) == []
assert quickSort([2]) == [2]
