def quickSort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    lowerEqVals = []
    higherVals = []
    for val in array[1:]:
        if val > pivot:
            higherVals.append(val)
        else:
            lowerEqVals.append(val)
    return quickSort(lowerEqVals) + [pivot] + quickSort(higherVals)


print(quickSort([0, 4, 2, 1, 98, 4, 2, 1, 0]))
