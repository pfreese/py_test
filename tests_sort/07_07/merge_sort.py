import sort_utils


def merge_two_sorted(ls1, ls2):
    l1 = len(ls1)
    l2 = len(ls2)

    result = [None for _ in range(l1 + l2)]

    i1 = 0
    i2 = 0
    ri = 0

    while i1 < l1 and i2 < l2:
        if ls1[i1] <= ls2[i2]:
            result[ri] = ls1[i1]
            i1 += 1
        else:
            result[ri] = ls2[i2]
            i2 += 1
        ri += 1

    while i1 < l1:
        result[ri] = ls1[i1]
        i1 += 1
        ri += 1
    while i2 < l2:
        result[ri] = ls2[i2]
        i2 += 1
        ri += 1
    return result


def merge_sort(array):

    if len(array) < 2:
        return array

    n2 = len(array) // 2

    l_half_sorted = merge_sort(array[:n2])
    r_half_sorted = merge_sort(array[n2:])

    return merge_two_sorted(l_half_sorted, r_half_sorted)




# TESTS

intsActual = merge_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = merge_sort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert merge_sort([]) == []
assert merge_sort([2]) == [2]
