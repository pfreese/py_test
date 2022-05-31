import sort_utils


def insertionSort(array) -> []:

    if len(array) < 2:
        return array

    for i in range(1, len(array)):
        j = i
        while j > 0:
            if array[j - 1] >= array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break
            j -= 1
    return array



def bucketSort(array):
    if len(array) < 2:
        return array
    nBuckets = len(array)
    bucketValsDict = {}
    for i in range(nBuckets):
        bucketValsDict[i] = []

    minVal = min(array)
    maxVal = max(array)
    rangeVals = maxVal - minVal

    for val in array:
        bucket = int(((val - minVal) / rangeVals) * nBuckets)
        if bucket == nBuckets:
            bucket -= 1
        assert bucket in bucketValsDict.keys()
        bucketValsDict[bucket].append(val)

    result = []
    for i in range(nBuckets):
        result += insertionSort(bucketValsDict[i])
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
