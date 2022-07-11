import sort_utils

def quick_sort(array):
    if len(array) < 2:
        return array
    pivot_val = array[0]

    pivot_leq = [x for x in array[1:] if x <= pivot_val]
    pivot_gr = [x for x in array[1:] if x > pivot_val]

    return quick_sort(pivot_leq) + [pivot_val] + quick_sort(pivot_gr)

# TESTS

intsActual = quick_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quick_sort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quick_sort([]) == []
assert quick_sort([2]) == [2]
