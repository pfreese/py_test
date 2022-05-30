import sort_utils


def countingSort(array):

    if len(array) < 2:
        return array

    assert all([isinstance(x, int) for x in array])

    minVal = min(array)
    maxVal = max(array)

    valRange = maxVal - minVal

    counts = [0 for _ in range(valRange + 1)]

    for v in array:
        counts[v - minVal] += 1
    # Get cumsum of counts.
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i-1]

    result = [None for _ in range(len(array))]
    # NOTE: must go in reverse order for sorting to be stable.
    for val in array[::-1]:
        countsIdx = val - minVal
        resultIdx = counts[countsIdx] - 1
        counts[countsIdx] -= 1
        result[resultIdx] = val
    return result



# TESTS

intsActual = countingSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert countingSort([]) == []
assert countingSort([2]) == [2]
