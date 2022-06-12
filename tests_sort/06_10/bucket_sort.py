import sort_utils


def insertionSort(vals):
    n = len(vals)
    if n < 2:
        return vals

    for i in range(1, n):
        j = i
        while j >= 1:
            if vals[j] >= vals[j - 1]:
                vals[j], vals[j - 1] = vals[j - 1], vals[j]
                j -= 1
            else:
                break
    for i in range(1, n):
        assert vals[i] >= vals[i-1]
    return vals

def bucketSort(array):
    n = len(array)
    if n < 2:
        return array
    bucketVals = {}
    bucketIdxs = list(range(n))
    for i in bucketIdxs:
        bucketVals[i] = []

    minVal = min(array)
    maxVal = max(array)

    valRange = maxVal - minVal
    if valRange == 0:
        return array

    for val in array:
        idx = int(((val - minVal)/valRange) * n)
        if idx == n:
            idx -= 1
        assert idx in bucketIdxs
        bucketVals[idx].append(val)

    result = []
    for idx in bucketIdxs:
        result += insertionSort(bucketVals[idx])
    return result




# TESTS

intsActual = bucketSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

floatsActual = bucketSort(sort_utils.unsortedFloats)
assert floatsActual == sort_utils.sortedFloats
print(floatsActual)

assert bucketSort([]) == []
assert bucketSort([2]) == [2]
