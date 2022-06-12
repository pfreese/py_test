import sort_utils


def mergedTwoSorted(sl1, sl2):
    l1 = len(sl1)
    l2 = len(sl2)

    i1 = 0
    i2 = 0
    ir = 0
    result = [None for _ in range(l1+l2)]
    while i1 < l1 and i2 < l2:
        if sl1[i1] <= sl2[i2]:
            result[ir] = sl1[i1]
            i1 += 1
        else:
            result[ir] = sl2[i2]
            i2 += 1
        ir += 1
    while i1 < l1:
        result[ir] = sl1[i1]
        i1 += 1
        ir += 1
    while i2 < l2:
        result[ir] = sl2[i2]
        i2 += 1
        ir += 1
    return result




def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    return mergedTwoSorted(mergeSort(left), mergeSort(right))


# TESTS

intsActual = mergeSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = mergeSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert mergeSort([]) == []
assert mergeSort([2]) == [2]
