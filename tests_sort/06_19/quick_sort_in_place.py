import sort_utils

def swap(array, p1, p2):
    array[p1], array[p2] = array[p2], array[p1]

def partition(array, left, right):
    # Note left and right are inclusive.
    assert left < right
    pivot_val = array[left]
    i = left + 1
    j = left + 1
    while j <= right:
        if array[j] <= pivot_val:
            swap(array, i, j)
            i += 1
        j += 1
    # Place pivot.
    pivot_index = i - 1
    swap(array, left, pivot_index)
    return pivot_index

def quicksort_helper(array, left, right):
    # Note left and right are inclusive.
    if right <= left:
        return
    pivot_index = partition(array, left, right)
    quicksort_helper(array, left, pivot_index - 1)
    quicksort_helper(array, pivot_index + 1, right)
    return



def quickSort(array):
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
