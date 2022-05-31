import sort_utils


def binarySearchHelper(array, val, lowerInc, upperInc):
    if upperInc < lowerInc:
        return False
    midIdx = (lowerInc + upperInc) // 2
    if array[midIdx] == val:
        return True
    elif array[midIdx] > val:
        return binarySearchHelper(array, val, lowerInc, midIdx - 1)
    else:
        return binarySearchHelper(array, val, midIdx + 1, upperInc)


def binarySearch(array, val):
    return binarySearchHelper(array, val, 0, len(array) - 1)


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
