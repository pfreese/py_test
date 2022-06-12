import sort_utils

def swap(array, lower, upper):
    array[lower], array[upper] = array[upper], array[lower]

def bubble_sort(array):
    if len(array) < 2:
        return array
    sorted = False
    last_sorted = len(array) - 1
    while not sorted:
        sorted = True
        for i in range(last_sorted):
            if array[i + 1] < array[i]:
                swap(array, i, i+1)
                sorted = False
        last_sorted -= 1

# TESTS

array = sort_utils.unsortedInts
bubble_sort(array)
assert array == sort_utils.sortedInts
print(array)

array = sort_utils.unsortedFloats
bubble_sort(array)
assert array == sort_utils.sortedFloats
print(array)

assert bubble_sort([]) == []
assert bubble_sort([2]) == [2]
