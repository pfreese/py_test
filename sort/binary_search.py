import sort_utils

def binary_search_recursive_helper(array, val, lower_inc, upper_inc):
    if upper_inc < lower_inc:
        return False
    midIdx = (lower_inc + upper_inc) // 2
    if array[midIdx] == val:
        return True
    elif array[midIdx] > val:
        return binary_search_recursive_helper(array, val, lower_inc, midIdx - 1)
    else:
        return binary_search_recursive_helper(array, val, midIdx + 1, upper_inc)

# Return TRUE/FALSE.
def binary_search_recursive(array, val):
    return binary_search_recursive_helper(array, val, 0, len(array) - 1)

# RETURN INDEX.
def binary_search_interative(array, val):
    if len(array) == 0:
        return -1
    lower = 0
    upper = len(array) - 1
    while lower <= upper:
        mid = lower + ((upper - lower )// 2)
        if array[mid] == val:
            return mid
        elif array[mid] < val:
            lower = mid + 1
        else:
            upper = mid - 1
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
