import sort_utils


def counting_sort(array):




# TESTS

intsActual = counting_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert counting_sort([]) == []
assert counting_sort([2]) == [2]
