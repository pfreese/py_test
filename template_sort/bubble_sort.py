import sort_utils


# Sort in place; don't return anything.
def bubble_sort(array):


# TESTS

array = sort_utils.unsortedInts
bubble_sort(array)
assert array == sort_utils.sortedInts
print(array)

array = sort_utils.unsortedFloats
bubble_sort(array)
assert array == sort_utils.sortedFloats
print(array)

assert bubble_sort([]) == []
assert bubble_sort([2]) == [2]
