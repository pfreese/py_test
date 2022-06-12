import sort_utils


def countingSort(array):
    n = len(array)
    if n < 2:
        return array
    minVal = min(array)
    maxVal = max(array)
    valRange = maxVal - minVal
    if valRange == 0:
        return array

    countIdxs = list(range(n))
    counts = [0 for _ in countIdxs]

    def valToCountIdx(val):
        countIdx = int(((val - minVal) / valRange) * n)
        if countIdx == n:
            countIdx -= 1
        assert countIdx in countIdxs
        return countIdx

    for val in array:
        counts[valToCountIdx(val)] += 1

    cumSumCounts = counts
    for i in range(1, n):
        cumSumCounts[i] = cumSumCounts[i] + cumSumCounts[i - 1]

    result = [None for _ in countIdxs]

    for val in array[::-1]:
        countIdx = valToCountIdx(val)
        idxPlusOne = counts[countIdx]
        counts[countIdx] -= 1
        assert result[idxPlusOne -  1] is None
        result[idxPlusOne -  1] = val
    return result




# TESTS

intsActual = countingSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert countingSort([]) == []
assert countingSort([2]) == [2]
