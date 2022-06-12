import sort_utils

def getMaskPow10(val, maskPow10):
    if val < maskPow10:
        return 0
    # e.g., val is: 987;
    valRemainder = val % (maskPow10 * 10)
    valAfterMask = valRemainder % maskPow10
    result = int((valRemainder - valAfterMask)/maskPow10)
    assert result in list(range(10))
    return result


def countingSortDigit(array, maskPow10):
    print(array)
    print(maskPow10)
    arrayTuple = [(x, getMaskPow10(x, maskPow10)) for x in array]

    # Perform counting sort.
    counts = [0 for _ in range(10)]
    for tupl in arrayTuple:
        counts[tupl[1]] += 1
    # Get cumulative sum.
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i-1]

    # Go through
    result = [None for _ in range(len(array))]
    for tupl in arrayTuple[::-1]:
        cumSum = counts[tupl[1]]
        counts[tupl[1]] -= 1
        result[cumSum - 1] = tupl[0]
    assert all([x is not None for x in result])
    return result


def nDigits(x):
    i = 1
    while True:
        if x < int(10 ** i):
            return i
        i += 1

def radixSort(array):
    if len(array) < 2:
        return array
    maxNDigits = max([nDigits(x) for x in array])
    print(maxNDigits)
    for i in range(maxNDigits):
        # maskPow10 is 1; 10; 100; etc.
        maskPow10 = int(10 ** i)
        # Counting sort for value in variable:
        array = countingSortDigit(array, maskPow10)
    return array


# TESTS

actual = radixSort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radixSort([]) == []
assert radixSort([2000]) == [2000]
