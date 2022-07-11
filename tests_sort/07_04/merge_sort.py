import sort_utils


def merge_two_sorted(sl1, sl2):
    l1 = len(sl1)
    l2 = len(sl2)

    i1 = 0
    i2 = 0

    result = [None for _ in range(l1 + l2)]
    ri = 0

    while i1 < l1 and i2 < l2:
        if sl1[i1] <= sl2[i2]:
            result[ri] = sl1[i1]
            i1 += 1
        else:
            result[ri] = sl2[i2]
            i2 += 1
        ri += 1
    while i1 < l1:
        result[ri] = sl1[i1]
        i1 += 1
        ri += 1
    while i2 < l2:
        result[ri] = sl2[i2]
        i2 += 1
        ri += 1
    return result


def merge_sort(array):
    n = len(array)
    if n < 2:
        return array
    h = len(array) // 2
    sorted_l = merge_sort(array[:h])
    sorted_r = merge_sort(array[h:])
    return merge_two_sorted(sorted_l, sorted_r)




# TESTS

intsActual = merge_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = merge_sort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert merge_sort([]) == []
assert merge_sort([2]) == [2]
