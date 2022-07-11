import sort_utils

def quickSort(array):
    n = len(array)
    if n < 2:
        return array

    pivot_val = array[0]

    leq_pivot_val = [x for x in array[1:] if x <= pivot_val]
    gr_pivot_val = [x for x in array[1:] if x > pivot_val]

    return quickSort(leq_pivot_val) + [pivot_val] + quickSort(gr_pivot_val)

# TESTS

intsActual = quickSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quickSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quickSort([]) == []
assert quickSort([2]) == [2]
