import sort_utils

def partition(array, lowerInc, upperInc):
    assert lowerInc < upperInc
    pivotVal = array[lowerInc]
    i = lowerInc + 1
    j = lowerInc + 1
    while j <= upperInc:
        if array[j] <= pivotVal:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1
    pivotIdx = i - 1
    array[lowerInc], array[pivotIdx] = array[pivotIdx], array[lowerInc]
    return pivotIdx


def quickSortRange(array, lowerInc, upperInc):
    if lowerInc >= upperInc:
        return
    pivotIdx = partition(array, lowerInc, upperInc)
    quickSortRange(array, lowerInc, pivotIdx - 1)
    quickSortRange(array, pivotIdx + 1, upperInc)
    return array


def quickSort(array):
    if len(array) < 2:
        return array
    return quickSortRange(array, 0, len(array) - 1)



# TESTS

intsActual = quickSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quickSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quickSort([]) == []
assert quickSort([2]) == [2]
