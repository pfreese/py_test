import sort_utils

def quick_sort(array):



# TESTS

intsActual = quick_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = quick_sort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert quick_sort([]) == []
assert quick_sort([2]) == [2]
