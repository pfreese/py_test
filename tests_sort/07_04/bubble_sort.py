import sort_utils


def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]

# Sort in place; don't return anything.
def bubble_sort(array):
    n = len(array)
    if n < 2:
        return True
    # want to bubble the greatest element.
    is_sorted = False
    round = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - round):
            if array[i] > array[i+1]:
                is_sorted = False
                swap(array, i, i+1)
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
