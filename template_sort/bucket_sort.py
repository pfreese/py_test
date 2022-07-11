import sort_utils



def bucket_sort(array):


# TESTS

intsActual = bucket_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = bucket_sort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert bucket_sort([]) == []
assert bucket_sort([2]) == [2]
