import sort_utils


def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]


def partition(array, lowerInc, upperInc):
    assert lowerInc < upperInc
    pivotVal = array[lowerInc]

    leqUpperIdx = lowerInc + 1
    checkIdx = lowerInc + 1
    while checkIdx <= upperInc:
        if array[checkIdx] <= pivotVal:
            swap(array, leqUpperIdx, checkIdx)
            leqUpperIdx += 1
        checkIdx += 1
    pivotIdx = leqUpperIdx - 1
    swap(array, lowerInc, pivotIdx)
    return pivotIdx


def quickSortRange(array, lowerInc, upperInc):
    if upperInc <= lowerInc:
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
