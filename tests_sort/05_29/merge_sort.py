import sort_utils


def mergeSorted(sorted1, sorted2):
    l1 = len(sorted1)
    l2 = len(sorted2)
    result = [None for _ in range(l1 + l2)]

    ir = 0
    i1 = 0
    i2 = 0
    while i1 < l1 and i2 < l2:
        if sorted1[i1] < sorted2[i2]:
            result[ir] = sorted1[i1]
            i1 += 1
        else:
            result[ir] = sorted2[i2]
            i2 += 1
        ir += 1
    # Remaining elements in 1 or 2.
    while i1 < l1:
        result[ir] = sorted1[i1]
        i1 += 1
        ir += 1
    while i2 < l2:
        result[ir] = sorted2[i2]
        i2 += 1
        ir += 1
    return result


def mergeSort(array):
    if len(array) < 2:
        return array
    i = len(array) // 2

    leftArray = array[:i]
    rightArray = array[i:]

    return mergeSorted(mergeSort(leftArray), mergeSort(rightArray))


# TESTS

intsActual = mergeSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = mergeSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert mergeSort([]) == []
assert mergeSort([2]) == [2]
