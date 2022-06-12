import sort_utils

def merge_two_sorted(sorted_1, sorted_2):
    l_1 = len(sorted_1)
    l_2 = len(sorted_2)

    result = [None for _ in range(l_1 + l_2)]

    r = 0

    i_1 = 0
    i_2 = 0
    while i_1 < l_1 and i_2 < l_2:
        if sorted_1[i_1] <= sorted_2[i_2]:
            result[r] = sorted_1[i_1]
            i_1 += 1
        else:
            result[r] = sorted_2[i_2]
            i_2 += 1
        r += 1
    # Finish out list 1 or 2 as necessary.
    while i_1 < l_1:
        result[r] = sorted_1[i_1]
        i_1 += 1
        r += 1
    while i_2 < l_2:
        result[r] = sorted_2[i_2]
        i_2 += 1
        r += 1
    return result



def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left_sorted = mergeSort(array[:mid])
    right_sorted = mergeSort(array[mid:])
    return merge_two_sorted(left_sorted, right_sorted)




# TESTS

intsActual = mergeSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = mergeSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert mergeSort([]) == []
assert mergeSort([2]) == [2]
