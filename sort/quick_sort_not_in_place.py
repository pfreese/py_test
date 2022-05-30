import sort_utils

def quickSort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    lowerEqVals = []
    higherVals = []
    for val in array[1:]:
        if val > pivot:
            higherVals.append(val)
        else:
            lowerEqVals.append(val)
    return quickSort(lowerEqVals) + [pivot] + quickSort(higherVals)

# TESTS

intsActual = quickSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quickSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quickSort([]) == []
assert quickSort([2]) == [2]
