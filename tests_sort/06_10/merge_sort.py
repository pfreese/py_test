import sort_utils

def mergedTwoSorted(ls1, ls2):
    l1 = len(ls1)
    l2 = len(ls2)
    i1 = 0
    i2 = 0
    result = [None for _ in range(l1 + l2)]
    ir = 0
    while i1 < l1 and i2 < l2:
        if ls1[i1] <= ls2[i2]:
            result[ir] = ls1[i1]
            i1 += 1
        else:
            result[ir] = ls2[i2]
            i2 += 1
        ir += 1
    # Remainders of ls1 and ls2.
    while i1 < l1:
        result[ir] = ls1[i1]
        i1 += 1
        ir += 1
    while i2 < l2:
        result[ir] = ls2[i2]
        i2 += 1
        ir += 1
    assert not any([x is None for x in result])
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
