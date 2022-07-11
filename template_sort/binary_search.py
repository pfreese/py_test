# Return TRUE/FALSE.
def binary_search_recursive(array, val):


# RETURN INDEX.
def binary_search_iterative(array, val):



# TEST RECURSIVE.
test_search_array = [-2.5, -2.5, 0, 1, 1.2, 10, 10, 100]
assert binary_search_recursive(test_search_array, -2.5)
assert binary_search_recursive(test_search_array, 0)
assert binary_search_recursive(test_search_array, 1)
assert binary_search_recursive(test_search_array, 1.2)
assert binary_search_recursive(test_search_array, 10)
assert binary_search_recursive(test_search_array, 100)
assert not binary_search_recursive(test_search_array, 101)
assert not binary_search_recursive(test_search_array, -3)
assert not binary_search_recursive(test_search_array, 1.1)

assert binary_search_recursive([-2, 3], -2)
assert binary_search_recursive([-2, 3], 3)
assert not binary_search_recursive([-2, 3], -3)

assert binary_search_recursive([-2.5], -2.5)
assert not binary_search_recursive([-2.5], 3)

assert not binary_search_recursive([], 3)


# TEST ITERATIVE.
assert binary_search_iterative(test_search_array, 3) == -1
assert binary_search_iterative(test_search_array, -2.5) == 1
assert binary_search_iterative(test_search_array, 0) == 2
assert binary_search_iterative(test_search_array, 1.2) == 4

assert binary_search_iterative(test_search_array, 100) == 7
assert binary_search_iterative(test_search_array, 101) == -1
