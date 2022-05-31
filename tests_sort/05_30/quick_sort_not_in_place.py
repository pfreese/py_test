import sort_utils

def quickSort(array):

    if len(array) < 2:
        return array

    pivotVal = array[0]
    lowerVals = [x for x in array[1:] if x <= pivotVal]
    greaterVals = [x for x in array[1:] if x > pivotVal]

    return quickSort(lowerVals) + [pivotVal] + quickSort(greaterVals)

# TESTS

intsActual = quickSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quickSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quickSort([]) == []
assert quickSort([2]) == [2]
