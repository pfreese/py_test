
def nextGreatestBinaryHelper(array, val, idxLeq, idxGreater):
    assert idxLeq < idxGreater
    assert array[idxLeq] <= val
    assert array[idxGreater] > val
    if (idxLeq + 1) == idxGreater:
        return array[idxGreater]
    mid = idxLeq + min(((idxGreater - idxLeq) // 2), 1)
    if array[mid] == val:
        return val
    elif array[mid] < val:
        return nextGreatestBinaryHelper(array, val, mid, idxGreater)
    else:
        return nextGreatestBinaryHelper(array, val, idxLeq, mid)


def nextGreatestBinary(array, val):
    n = len(array)
    if n == 0:
        return -1
    if array[0] >= val:
        return array[0]
    if array[n-1] < val:
        return -1
    return nextGreatestBinaryHelper(array, val, 0, n - 1)


# def nextGreatestBinaryRange(array, val, lowerInc, upperInc):
#
#     if lowerInc == upperInc:
#         if lowerInc == len(array) - 1:
#             return -1
#         else:
#             nextGreatest = array[lowerInc + 1]
#             assert nextGreatest >= val
#             return nextGreatest
#     mid = lowerInc + ((upperInc - lowerInc) // 2)
#     if array[mid] == val:
#         return val
#     elif array[mid] > val:
#         return nextGreatestBinaryRange(array, val, lowerInc, mid - 1)
#     else:
#         # array[mid] <
#         if mid < (len(array) - 1):
#             if array[mid+1] >= val:
#                 return array[mid+1]
#         return nextGreatestBinaryRange(array, val, mid + 1, upperInc)
#
#
# def nextGreatestBinary(array, val):
#
#     # Want to find index i such that
#     # array[i] <= val and array[i+1] >= 1
#
#     return nextGreatestBinaryRange(array, val, 0, len(array) - 1)

print(nextGreatestBinary([1, 1, 4, 4, 7, 10, 100], 1)) #1
print(nextGreatestBinary([1, 1, 4, 4, 7, 10, 100], 2)) #4
print(nextGreatestBinary([1, 1, 4, 4, 7, 10, 100], 3)) #4
print(nextGreatestBinary([1, 1, 4, 4, 7, 10, 100], 4)) #4
print(nextGreatestBinary([1, 1, 4, 4, 7, 10, 100], 5)) #7
print(nextGreatestBinary([1, 1, 4, 4, 7, 10, 100], 6))
print(nextGreatestBinary([1, 1, 4, 4, 7, 10, 100], 7))
print(nextGreatestBinary([1, 1, 4, 4, 7, 10, 100], 8))
