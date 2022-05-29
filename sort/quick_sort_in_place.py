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


print(quickSort([4, 7, 1, 2, 10, 4, 8, 0, 0, 1, 4, 0]))

print(quickSort([5, 2, 1, 1.2, 0, 9, 7, 9]))
print(quickSort([0]))
print(quickSort([]))
