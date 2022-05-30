import sort_utils


def mergeSort(array):



# TESTS

intsActual = mergeSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = mergeSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert mergeSort([]) == []
assert mergeSort([2]) == [2]
