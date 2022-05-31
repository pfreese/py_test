import sort_utils

def isPow10(pow10):
    exp = 0
    while ((10 ** exp) <= pow10):
        if (pow10 % int(10 ** exp)) != 0:
            return False
        exp += 1
    return True


def extractValAtPow10(val, pow10):
    assert isPow10(pow10)
    valLessBefore = val % int(pow10 * 10)

    remainder = valLessBefore % pow10

    valAtPow = int((valLessBefore - remainder) / pow10)
    assert valAtPow in range(10)
    return valAtPow



def countingSortPow10(array, pow10):
    assert isPow10(pow10)

    counts = [0 for _ in range(10)]

    # Get counts.
    for val in array:
        idx = extractValAtPow10(val, pow10)
        counts[idx] += 1

    # Get cumulative counts.
    for i in range(1, 10):
        counts[i] = counts[i] + counts[i-1]

    arraySorted = [None for _ in range(len(array))]

    for val in array[::-1]:
        idx = extractValAtPow10(val, pow10)
        idxToInsert = counts[idx] - 1
        counts[idx] -= 1
        arraySorted[idxToInsert] = val
    assert all([x is not None for x in arraySorted])

    return arraySorted



def radixSort(array):
    if len(array) < 2:
        return array

    # QC: all non-negative integers.
    assert all([isinstance(x, int) for x in array])
    assert all([x >= 0 for x in array])

    maxVal = max(array)
    if maxVal == 0:
        return array

    pow10 = 1
    while (maxVal // pow10) > 0:
        array = countingSortPow10(array, pow10)
        pow10 *= 10
    return array


# TESTS

actual = radixSort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radixSort([]) == []
assert radixSort([2000]) == [2000]
