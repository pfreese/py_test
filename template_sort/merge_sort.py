import sort_utils



def merge_sort(array):




# TESTS

intsActual = merge_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = merge_sort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert merge_sort([]) == []
assert merge_sort([2]) == [2]
