import sort_utils

def merge_two_sorted(sl1, sl2):
    l1 = len(sl1)
    l2 = len(sl2)

    result = [None for _ in range(l1 + l2)]
    ri = 0

    i1 = 0
    i2 = 0

    while i1 < l1 and i2 < l2:
        if sl1[i1] < sl2[i2]:
            result[ri] = sl1[i1]
            i1 += 1
        else:
            result[ri] = sl2[i2]
            i2 += 1
        ri += 1
    # Finish out sl1 (if any remaining).
    while i1 < l1:
        result[ri] = sl1[i1]
        i1 += 1
        ri += 1

    # Finish out sl2 (if any remaining).
    while i2 < l2:
        result[ri] = sl2[i2]
        i2 += 1
        ri += 1
    assert not any([x is None for x in result])
    return result

def mergesort_helper(array, left, right):
    if right < left:
        return []
    if right == left:
        return [array[left]]
    mid = left + ((right - left) // 2)
    left_sorted = mergesort_helper(array, left, mid)
    right_sorted = mergesort_helper(array, mid + 1, right)
    return merge_two_sorted(left_sorted, right_sorted)




def mergeSort(array):
    array = mergesort_helper(array, 0, len(array) - 1)
    return array



# TESTS

intsActual = mergeSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = mergeSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert mergeSort([]) == []
assert mergeSort([2]) == [2]
