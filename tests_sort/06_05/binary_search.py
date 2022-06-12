import sort_utils

def binarySearchRange(array, val, lowerInc, upperInc):
    if upperInc < lowerInc:
        return False
    mid = lowerInc + (upperInc - lowerInc) // 2
    if array[mid] == val:
        return True
    elif array[mid] < val:
        return binarySearchRange(array, val, mid+1, upperInc)
    else:
        return binarySearchRange(array, val, lowerInc, mid - 1)


def binarySearch(array, val):
    if len(array) == 0:
        return False
    return binarySearchRange(array, val, 0, len(array) - 1)


# TESTS

testSearchArray = [-2.5, -2.5, 0, 1, 1.2, 10, 10, 100]
assert(binarySearch(testSearchArray, -2.5))
assert(binarySearch(testSearchArray, 0))
assert(binarySearch(testSearchArray, 1))
assert(binarySearch(testSearchArray, 1.2))
assert(binarySearch(testSearchArray, 10))
assert(binarySearch(testSearchArray, 100))
assert(not binarySearch(testSearchArray, 101))
assert(not binarySearch(testSearchArray, -3))
assert(not binarySearch(testSearchArray, 1.1))

# Tests of small length.
assert(binarySearch([-2, 3], -2))
assert(binarySearch([-2, 3], 3))
assert(not binarySearch([-2, 3], -3))

assert(binarySearch([-2.5], -2.5))
assert(not binarySearch([-2.5], 3))

assert(not binarySearch([], 3))
