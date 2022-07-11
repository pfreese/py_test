import sort_utils

def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]


# Sort in place; don't return anything.
def bubble_sort(array):

    n = len(array)
    if n < 2:
        return array

    # Bubble up the greatest value each time.
    sorted = False
    round = 0
    while not sorted:
        sorted = True
        for i in range(n - round - 1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                sorted = False
        round += 1

    return array


# TESTS

array = sort_utils.unsortedInts
bubble_sort(array)
assert array == sort_utils.sortedInts
print(array)

array = sort_utils.unsortedFloats
bubble_sort(array)
assert array == sort_utils.sortedFloats
print(array)

array = []
bubble_sort(array)
assert array == []

array = [2]
bubble_sort(array)
assert array == [2]
