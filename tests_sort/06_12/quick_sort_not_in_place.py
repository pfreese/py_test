import sort_utils

def quickSort(array):
    if len(array) < 2:
        return array
    pivot_val = array[0]
    less_equal_pivot = [x for x in array[1:] if x <= pivot_val]
    greater_pivot = [x for x in array[1:] if x > pivot_val]
    return quickSort(less_equal_pivot) + [pivot_val] + quickSort(greater_pivot)

# TESTS

intsActual = quickSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quickSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quickSort([]) == []
assert quickSort([2]) == [2]
