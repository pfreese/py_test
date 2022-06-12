def binary_search_recursive_helper(array, val, lower, upper):
    if upper < lower:
        return False
    mid = lower + ((upper - lower) // 2)
    if array[mid] == val:
        return True
    elif array[mid] < val:
        return binary_search_recursive_helper(array, val, mid + 1, upper)
    else:
        return binary_search_recursive_helper(array, val, lower, mid - 1)

# Return TRUE/FALSE.
def binary_search_recursive(array, val):
    return binary_search_recursive_helper(array, val, 0, len(array) - 1)

def get_lowest_idx(array, idx):
    val = array[idx]
    lowest_idx = idx
    while idx > 0:
        idx -= 1
        if array[idx] == val:
            lowest_idx = idx
        else:
            break
    return lowest_idx

test_search_array = [-2.5, -2.5, 0, 1, 1.2, 10, 10, 100]
assert get_lowest_idx(test_search_array, 0) == 0
assert get_lowest_idx(test_search_array, 1) == 0
assert get_lowest_idx(test_search_array, 2) == 2
assert get_lowest_idx(test_search_array, 3) == 3
assert get_lowest_idx(test_search_array, 4) == 4
assert get_lowest_idx(test_search_array, 5) == 5
assert get_lowest_idx(test_search_array, 6) == 5
assert get_lowest_idx(test_search_array, 7) == 7


# RETURN INDEX.
def binary_search_interative(array, val):
    n = len(array)
    if n == 0:
        return -1
    lower = 0
    upper = n - 1
    while upper >= lower:
        mid = lower + ((upper - lower) // 2)
        if array[mid] == val:
            return get_lowest_idx(array, mid)
        elif array[mid] > val:
            upper = mid - 1
        else:
            lower = mid + 1
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
assert binary_search_interative(test_search_array, -2.5) == 0
assert binary_search_interative(test_search_array, 0) == 2
assert binary_search_interative(test_search_array, 1.2) == 4
assert binary_search_interative(test_search_array, 10) == 5
assert binary_search_interative(test_search_array, 100) == 7
assert binary_search_interative(test_search_array, 101) == -1
