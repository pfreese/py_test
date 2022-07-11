import sort_utils

def quickSort(array):
    if len(array) < 2:
        return array
    pivot_val = array[0]
    array_leq = [x for x in array[1:] if x <= pivot_val]
    array_gr = [x for x in array[1:] if x > pivot_val]
    return quickSort(array_leq) + [pivot_val] + quickSort(array_gr)

# TESTS

intsActual = quickSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quickSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quickSort([]) == []
assert quickSort([2]) == [2]
