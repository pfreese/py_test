import sort_utils


def countingSort(array):
    if len(array) < 2:
        return array
    # QC: array is all integers.
    assert all([isinstance(x, int) for x in array])

    minVal = min(array)
    maxVal = max(array)
    if minVal == maxVal:
        return array

    counts = [0 for _ in range(maxVal - minVal + 1)]

    for val in array:
        idx = val - minVal
        counts[idx] += 1

    # Get cumulative counts.
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i-1]

    result = [None for _ in range(len(array))]

    for val in array[::-1]:
        countsIdx = val - minVal
        resultIdx = counts[countsIdx] - 1
        counts[countsIdx] -= 1
        assert result[resultIdx] is None
        result[resultIdx] = val

    return result

# TESTS

intsActual = countingSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert countingSort([]) == []
assert countingSort([2]) == [2]
