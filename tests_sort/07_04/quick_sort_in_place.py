import sort_utils

def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]

def partition(array, lower, upper):
    assert lower < upper
    pivot_val = array[lower]

    i = lower + 1
    j = lower + 1
    while j <= upper:
        if array[j] <= pivot_val:
            swap(array, i, j)
            i += 1
        j += 1
    pivot_idx = i - 1
    swap(array, lower, pivot_idx)
    return pivot_idx

def quick_sort_helper(array, lower, upper):
    if upper <= lower:
        return
    pivot_idx = partition(array, lower, upper)
    quick_sort_helper(array, lower, pivot_idx - 1)
    quick_sort_helper(array, pivot_idx + 1, upper)
    return

def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array



# TESTS

intsActual = quick_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quick_sort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quick_sort([]) == []
assert quick_sort([2]) == [2]
