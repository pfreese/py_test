import sort_utils


def extractDigit(x, pow10):
    ensurePow10(pow10)
    xPow10AndAfter = x % int(10 * pow10)

    return int((xPow10AndAfter - (xPow10AndAfter % pow10)) / pow10)

def countingSortPow10(array, pow10):
    ensurePow10(pow10)
    # Remove the portion before the power of 10.
    arrayWDigits = [(x, extractDigit(x, pow10)) for x in array]

    # Perform counting sort.
    counts = [0 for _ in range(10)]
    for t in arrayWDigits:
        counts[t[1]] += 1
    # Get cumulative counts.
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i-1]

    result = [None for _ in range(len(array))]

    for t in reversed(arrayWDigits):
        idx = counts[t[1]] - 1
        assert idx in list(range(len(array)))
        assert result[idx] is None
        counts[t[1]] -= 1
        result[idx] = t[0]

    # Check all list elements were populated.
    assert all([x is not None for x in result])
    return result



def ensurePow10(x):
    assert x == int(10 ** (nDigits(x) - 1))



def nDigits(x):
    i = 1
    while True:
        if x < int(10 ** i):
            return i
        i += 1

def radixSort(array):
    if len(array) < 2:
        return array

    # QC: non-negative integers.
    assert all([isinstance(x, int) for x in array])
    assert all([x >= 0 for x in array])

    #
    maxNDigits = max([nDigits(x) for x in array])

    for exponent in range(maxNDigits):
        # pow10 is 1, 10, 100, etc.
        pow10 = int(10 ** exponent)

        array = countingSortPow10(array, pow10)
    return array

# TESTS

actual = radixSort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radixSort([]) == []
assert radixSort([2000]) == [2000]
