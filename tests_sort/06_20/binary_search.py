
def binary_search_recursive_helper(array, val, lower, upper):
    if upper < lower:
        return False
    mid = lower + ((upper - lower) // 2)
    if array[mid] == val:
        return True
    elif val < array[mid]:
        return binary_search_recursive_helper(array, val, lower, mid - 1)
    else:
        return binary_search_recursive_helper(array, val, mid + 1, upper)

# Return TRUE/FALSE.
def binary_search_recursive(array, val):
    return binary_search_recursive_helper(array, val, 0, len(array) - 1)


# RETURN INDEX.
def binary_search_interative(array, val):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + ((right - left) // 2)
        if array[mid] == val:
            return mid
        elif val < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1



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
assert binary_search_interative(test_search_array, 3) == -1
assert binary_search_interative(test_search_array, -2.5) == 1
assert binary_search_interative(test_search_array, 0) == 2
assert binary_search_interative(test_search_array, 1.2) == 4

assert binary_search_interative(test_search_array, 100) == 7
assert binary_search_interative(test_search_array, 101) == -1
