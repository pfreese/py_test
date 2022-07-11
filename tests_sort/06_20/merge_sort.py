import sort_utils

def merge_two_sorted(a1, a2):
    l1 = len(a1)
    l2 = len(a2)
    i1 = 0
    i2 = 0

    result = [None for _ in range(l1 + l2)]
    ir = 0
    while i1 < l1 and i2 < l2:
        if a1[i1] <= a2[i2]:
            result[ir] = a1[i1]
            i1 += 1
        else:
            result[ir] = a2[i2]
            i2 += 1
        ir += 1
    # Remainder of a1, if any.
    while i1 < l1:
        result[ir] = a1[i1]
        i1 += 1
        ir += 1
    # Remainder of a2, if any.
    while i2 < l2:
        result[ir] = a2[i2]
        i2 += 1
        ir += 1
    return result


def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left_array = mergeSort(array[:mid])
    right_array = mergeSort(array[mid:])
    return merge_two_sorted(left_array, right_array)



# TESTS

intsActual = mergeSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = mergeSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert mergeSort([]) == []
assert mergeSort([2]) == [2]
