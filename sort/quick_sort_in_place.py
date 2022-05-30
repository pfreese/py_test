import sort_utils

# Partion array from [lowerInc, upperInc] (inclusive on both ends),
# and return index where pivot element was placed.
def partition(array, lowerInc, upperInc):

    assert lowerInc < upperInc
    pivotVal = array[lowerInc]
    i, j = lowerInc + 1, lowerInc + 1

    while j <= upperInc:
        if array[j] <= pivotVal:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    array[i-1], array[lowerInc] = array[lowerInc], array[i-1]
    return i-1


def quicksortPartial(array, lowerInc, upperInc):
    if upperInc <= lowerInc:
        return
    assert lowerInc < upperInc, f"Failure in quicksortPartial(): {lowerInc} vs. {upperInc}"

    i = partition(array, lowerInc, upperInc)
    quicksortPartial(array, lowerInc, i-1)
    quicksortPartial(array, i+1, upperInc)


def quickSort(array):

    quicksortPartial(array, 0, len(array) - 1)
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
