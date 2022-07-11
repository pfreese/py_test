import sort_utils


def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]

# Sort in place; don't return anything.
def bubble_sort(array):
    n = len(array)
    if n < 2:
        return

    for round_i in range(n - 1):
        is_sorted = True
        j = 0
        while j < (n - round_i - 1):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
                is_sorted = False
            j += 1
        if is_sorted:
            return
    return



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
