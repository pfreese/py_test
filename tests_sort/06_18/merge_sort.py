import sort_utils

def merge_two_sorted_lists(array_1, array_2):
    l_1 = len(array_1)
    l_2 = len(array_2)

    i_1 = 0
    i_2 = 0

    result = [None for _ in range(l_1 + l_2)]
    r_i = 0
    while (i_1 < l_1) and (i_2 < l_2):
        if (array_1[i_1] <= array_2[i_2]):
            result[r_i] = array_1[i_1]
            i_1 += 1
        else:
            result[r_i] = array_2[i_2]
            i_2 += 1
        r_i += 1
    while (i_1 < l_1):
        result[r_i] = array_1[i_1]
        i_1 += 1
        r_i += 1
    while (i_2 < l_2):
        result[r_i] = array_2[i_2]
        i_2 += 1
        r_i += 1
    return result



def mergeSort(array):
    n = len(array)
    if n < 2:
        return array

    mid = n // 2
    left = array[:mid]
    right = array[mid:]

    return merge_two_sorted_lists(mergeSort(left), mergeSort(right))



# TESTS

intsActual = mergeSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = mergeSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert mergeSort([]) == []
assert mergeSort([2]) == [2]
