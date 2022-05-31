import sort_utils

def mergeTwoSorted(array1, array2):
    len1 = len(array1)
    len2 = len(array2)

    result = [None for _ in range(len1 + len2)]

    i1 = 0
    i2 = 0

    ir = 0
    while i1 < len1 and i2 < len2:
        if array1[i1] <= array2[i2]:
            result[ir] = array1[i1]
            i1 += 1
        else:
            result[ir] = array2[i2]
            i2 += 1
        ir += 1

    while i1 < len1:
        result[ir] = array1[i1]
        i1 += 1
        ir += 1

    while i2 < len2:
        result[ir] = array2[i2]
        i2 += 1
        ir += 1

    return result


def mergeSort(array):
    if len(array) < 2:
        return array

    i = len(array) // 2
    return mergeTwoSorted(mergeSort(array[:i]), mergeSort(array[i:]))


# TESTS

intsActual = mergeSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = mergeSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert mergeSort([]) == []
assert mergeSort([2]) == [2]
