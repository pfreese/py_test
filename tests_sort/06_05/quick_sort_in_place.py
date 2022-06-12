import sort_utils


def partition(array, lowerInc, upperInc):
    assert lowerInc < upperInc
    partitionVal = array[lowerInc]
    i = lowerInc + 1
    j = lowerInc + 1
    while j <= upperInc:
        if array[j] <= partitionVal:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    # Place the partition value.
    array[lowerInc], array[i - 1] = array[i - 1], array[lowerInc]
    return i - 1


def quickSortRange(array, lowerInc, upperInc):
    if lowerInc >= upperInc:
        return
    pivotIdx = partition(array, lowerInc, upperInc)
    quickSortRange(array, lowerInc, pivotIdx - 1)
    quickSortRange(array, pivotIdx + 1, upperInc)
    return


def quickSort(array):
    if len(array) < 2:
        return array
    # Quick sort a range
    quickSortRange(array, 0, len(array) - 1)
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
