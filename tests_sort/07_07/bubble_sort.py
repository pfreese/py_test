import sort_utils

def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]

# Sort in place; don't return anything.
def bubble_sort(array):

    n = len(array)
    if n < 2:
        return

    is_sorted = False
    i = 0
    while not is_sorted:
        is_sorted = True
        for lower_idx in range(n - i - 1):
            if array[lower_idx + 1] < array[lower_idx]:
                is_sorted = False
                swap(array, lower_idx, lower_idx + 1)
        i += 1
    return


# TESTS

array = sort_utils.unsortedInts
print(array)
bubble_sort(array)
print(array)
assert array == sort_utils.sortedInts


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
