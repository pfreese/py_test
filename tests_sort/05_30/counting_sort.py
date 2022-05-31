import sort_utils


def countingSort(array):
    if len(array) < 2:
        return array
    assert all([isinstance(x, int) for x in array])

    minVal = min(array)
    maxVal = max(array)

    nCountBins = maxVal - minVal + 1
    countBins = list(range(nCountBins))

    counts = [0 for _ in range(nCountBins)]

    for val in array:
        countBin = val - minVal
        assert countBin in countBins
        counts[countBin] += 1

    # Get the cumulative sum.
    for i in range(1, nCountBins):
        counts[i] = counts[i] + counts[i - 1]

    result = [None for _ in range(len(array))]
    for val in array[::-1]:
        countBin = val - minVal
        assert countBin in countBins
        idx = counts[countBin] - 1
        counts[countBin] -= 1
        result[idx] = val

    return result


# TESTS

intsActual = countingSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert countingSort([]) == []
assert countingSort([2]) == [2]
