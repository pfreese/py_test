import sort_utils


def partition(array, lowerInc, upperInc):
    assert lowerInc < upperInc
    partitionVal = array[lowerInc]
    i = lowerInc + 1
    j = lowerInc + 1
    while j <= upperInc:
        if array[j] <= partitionVal:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1
    array[lowerInc], array[i-1] = array[i-1], array[lowerInc]
    return i-1

def quickSortRange(array, lowerInc, upperInc):
    if lowerInc >= upperInc:
        return array
    partitionIdx = partition(array, lowerInc, upperInc)
    array = quickSortRange(array, lowerInc, partitionIdx - 1)
    array = quickSortRange(array, partitionIdx + 1, upperInc)
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
