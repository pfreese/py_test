import sort_utils

def radix_sort(array):


# TESTS

actual = radix_sort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radix_sort([]) == []
assert radix_sort([2000]) == [2000]
