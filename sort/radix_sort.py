import sort_utils

import math

def isPow10(digit):
    assert digit > 0
    return digit == int(10 ** math.floor(math.log10(digit)))

def getDigit(val, digit):
    assert isPow10(digit)
    if val < digit:
        return 0
    valWithoutPreceding = val % (10 * digit)
    result = int((valWithoutPreceding - (valWithoutPreceding % digit)) / digit)
    assert result in list(range(10))

    return result


def countingSort(array, digit):
    assert isPow10(digit)

    counts = [0 for _ in range(10)]

    for val in array:
        counts[getDigit(val, digit)] += 1
    # Calculate cumsum.
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i - 1]

    result = [None for _ in range(len(array))]
    # NOTE: must go in reverse order to preserve
    for val in array[::-1]:
        countsIdx = getDigit(val, digit)
        resultIdx = counts[countsIdx] - 1
        result[resultIdx] = val
        counts[countsIdx] -= 1
    assert all([x is not None for x in result])
    return result


def radixSort(array):

    if len(array) < 2:
        return array

    assert(all([isinstance(x, int) for x in array]))
    assert(all([x >= 0 for x in array]))

    maxVal = max(array)
    if maxVal == 0:
        return array

    nDigits = math.floor(math.log10(maxVal))

    digit = 1
    while (maxVal // digit) > 0:
        array = countingSort(array, digit)
        digit *= 10

    return array



# TESTS

actual = radixSort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radixSort([]) == []
assert radixSort([2000]) == [2000]
