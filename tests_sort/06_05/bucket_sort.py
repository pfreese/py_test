import sort_utils


def insertionSort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        j = i
        while j >= 1:
            if array[j] >= array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1
            else:
                break
    return array


def bucketSort(array):
    if len(array) < 2:
        return array

    nVals = len(array)

    minVal = min(array)
    maxVal = max(array)
    valRange = maxVal - minVal
    if valRange == 0:
        return array

    buckets = {}
    for i in range(nVals):
        buckets[i] = []

    # Go through each value, get its bucket, and add the
    # value to that bucket.
    for val in array:
        bucket = int(((val - minVal) / valRange) * nVals)
        if bucket == nVals:
            bucket -= 1
        assert bucket in list(range(nVals))
        buckets[bucket].append(val)

    result = []
    for i in range(nVals):
        result += insertionSort(buckets[i])
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
