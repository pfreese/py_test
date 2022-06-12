import sort_utils

def swap(array, p1, p2):
    array[p1], array[p2] = array[p2], array[p1]
    return

# Sort in place; don't return anything.
def bubble_sort(array):
    n = len(array)
    if n < 2:
        return
    sorted = False
    greatest = n - 1
    while not sorted:
        sorted = True
        for i in range(greatest):
            if array[i+1] < array[i]:
                swap(array, i, i+1)
                sorted = False
        greatest -= 1
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
