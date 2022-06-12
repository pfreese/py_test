import sort_utils


def countingSort(array):
    if len(array) < 2:
        return array
    minVal = min(array)
    maxVal = max(array)
    valRange = maxVal - minVal
    if valRange == 0:
        return array

    counts = [0 for _ in range(valRange + 1)]

    for val in array:
        idx = val - minVal
        counts[idx] += 1
    # Get cumulative counts.
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i-1]

    result = [None for _ in range(len(array))]
    for val in reversed(array):
        countsIdx = val - minVal
        assert countsIdx in list(range(len(counts)))
        resultIdx = counts[countsIdx] - 1
        counts[countsIdx] -= 1
        assert resultIdx in list(range(len(result)))
        assert result[resultIdx] is None
        result[resultIdx] = val
    assert all([x is not None for x in result])
    return result





# TESTS

intsActual = countingSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert countingSort([]) == []
assert countingSort([2]) == [2]
