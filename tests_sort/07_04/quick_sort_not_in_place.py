import sort_utils

def quick_sort(array):
    n = len(array)
    if n < 2:
        return array
    pivot_val = array[0]

    leq = [x for x in array[1:] if x <= pivot_val]
    g = [x for x in array[1:] if x > pivot_val]

    return quick_sort(leq) + [pivot_val] + quick_sort(g)

# TESTS

intsActual = quick_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quick_sort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quick_sort([]) == []
assert quick_sort([2]) == [2]
