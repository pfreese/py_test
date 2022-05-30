import sort_utils


def countingSort(array):



# TESTS

intsActual = countingSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert countingSort([]) == []
assert countingSort([2]) == [2]
