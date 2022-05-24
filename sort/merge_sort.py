def mergeTwoSorted(s1, s2):
    result = [None]*(len(s1) + len(s2))
    s1_i = 0
    s2_i = 0
    r_i = 0
    while s1_i < len(s1) and s2_i < len(s2):
        if s1[s1_i] < s2[s2_i]:
            result[r_i] = s1[s1_i]
            s1_i += 1
        else:
            result[r_i] = s2[s2_i]
            s2_i += 1
        r_i += 1
    while s1_i < len(s1):
        result[r_i] = s1[s1_i]
        s1_i += 1
        r_i += 1
    while s2_i < len(s2):
        result[r_i] = s2[s2_i]
        s2_i += 1
        r_i += 1
    return result

def mergeSort(vals):

    if len(vals) < 2:
        return vals

    mid = len(vals) // 2

    sortedLowerHalf = mergeSort(vals[:mid])
    sortedUpperHalf = mergeSort(vals[mid:])

    return mergeTwoSorted(sortedLowerHalf, sortedUpperHalf)


print(mergeSort([0, 4, 2, 1, 98, 4, 2, 1, 0]))
