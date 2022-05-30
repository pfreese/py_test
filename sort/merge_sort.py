import sort_utils

def mergeTwoSorted(s1, s2):
    result = [None]*(len(s1) + len(s2))
    s1_i = 0
    s2_i = 0
    r_i = 0
    while s1_i < len(s1) and s2_i < len(s2):
        if s1[s1_i] < s2[s2_i]:
            result[r_i] = s1[s1_i]
            s1_i += 1
        else:
            result[r_i] = s2[s2_i]
            s2_i += 1
        r_i += 1
    while s1_i < len(s1):
        result[r_i] = s1[s1_i]
        s1_i += 1
        r_i += 1
    while s2_i < len(s2):
        result[r_i] = s2[s2_i]
        s2_i += 1
        r_i += 1
    return result

def mergeSort(array):

    if len(array) < 2:
        return array

    mid = len(array) // 2

    sortedLowerHalf = mergeSort(array[:mid])
    sortedUpperHalf = mergeSort(array[mid:])

    return mergeTwoSorted(sortedLowerHalf, sortedUpperHalf)

# TESTS

intsActual = mergeSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = mergeSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert mergeSort([]) == []
assert mergeSort([2]) == [2]
