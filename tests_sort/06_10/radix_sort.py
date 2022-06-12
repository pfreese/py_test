import sort_utils

from collections import namedtuple

xWithDigit = namedtuple('xWithDigit', ['x', 'digit'])

def getDigit(x, pow10Mask):
    xWMask = x % int(10 * pow10Mask)
    xOnly = xWMask - (xWMask % pow10Mask)
    return int(xOnly / pow10Mask)

assert(getDigit(456, 1) == 6)
assert(getDigit(456, 10) == 5)
assert(getDigit(456, 100) == 4)
assert(getDigit(456, 1000) == 0)

def sortOnPow10Mask(array, pow10Mask):

    arrayWDigits = [xWithDigit(x, getDigit(x, pow10Mask)) for x in array]

    counts = [0 for _ in range(10)]
    for xWithDig in arrayWDigits:
        counts[xWithDig.digit] += 1

    # Convert to cumsum.
    cumSumCounts = counts
    for i in range(1, len(cumSumCounts)):
        cumSumCounts[i] = cumSumCounts[i] + cumSumCounts[i-1]

    result = [None for _ in range(len(array))]
    for xWithDig in arrayWDigits[::-1]:
        idxPlus1 = cumSumCounts[xWithDig.digit]
        assert idxPlus1 >= 1
        cumSumCounts[xWithDig.digit] -= 1
        assert result[idxPlus1 - 1] is None
        result[idxPlus1 - 1] = xWithDig.x
    assert all([x is not None for x in result])
    return result


def nDigits(x):
    nDigits = 1
    while True:
        if (x + 1) <= int(10 ** nDigits):
            return nDigits
        nDigits += 1

assert nDigits(0) == 1
assert nDigits(9) == 1
assert nDigits(10) == 2
assert nDigits(99) == 2
assert nDigits(100) == 3


def radixSort(array):
    if len(array) < 2:
        return array
    # Assume all values are non-negative integers.
    maxNDigits = max([nDigits(x) for x in array])

    for digitIndex in range(maxNDigits):
        # pow10Mask will be 1, 10, 100, etc.
        pow10Mask = int(10 ** digitIndex)
        array = sortOnPow10Mask(array, pow10Mask)
    return array


# TESTS

actual = radixSort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radixSort([]) == []
assert radixSort([2000]) == [2000]
