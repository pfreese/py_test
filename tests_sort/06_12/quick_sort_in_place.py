import sort_utils

def swap(array, p1, p2):
    array[p1], array[p2] = array[p2], array[p1]

# Want to pick a pivot element.
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
    pivot_idx = i - 1
    swap(array, pivot_idx, lower)
    return pivot_idx

def quick_sort_range(array, lower, upper):
    if upper <= lower:
        return
    pivot_idx = partition(array, lower, upper)
    quick_sort_range(array, lower, pivot_idx - 1)
    quick_sort_range(array, pivot_idx + 1, upper)
    return

def quickSort(array):
    n = len(array)
    if n < 2:
        return array
    quick_sort_range(array, 0, n - 1)
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
