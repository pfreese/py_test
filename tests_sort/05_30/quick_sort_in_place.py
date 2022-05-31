import sort_utils


def partition(array, lowerIdxInc, upperIdxInc):
    assert lowerIdxInc < upperIdxInc

    pivotVal = array[lowerIdxInc]

    i = lowerIdxInc + 1
    j = lowerIdxInc + 1

    while j <= upperIdxInc:
        if array[j] <= pivotVal:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1
    array[lowerIdxInc], array[i-1] = array[i-1], array[lowerIdxInc]

    return i-1


def quickSortRange(array, lowerIdxInc, upperIdxInc):
    if upperIdxInc <= lowerIdxInc:
        return array
    pivotIdx = partition(array, lowerIdxInc, upperIdxInc)
    array = quickSortRange(array, lowerIdxInc, pivotIdx - 1)
    array = quickSortRange(array, pivotIdx + 1, upperIdxInc)

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
