import sort_utils


def counting_sort(array):
    n = len(array)
    if n < 2:
        return array

    min_val = min(array)
    max_val = max(array)
    val_range = max_val - min_val
    if val_range == 0:
        return array

    counts = [0 for _ in range(val_range + 1)]
    for val in array:
        idx = val - min_val
        counts[idx] += 1

    cum_counts = counts
    for i in range(1, val_range + 1):
        cum_counts[i] = cum_counts[i] + cum_counts[i-1]

    result = [None for _ in range(n)]
    for val in array[::-1]:
        idx = val - min_val
        result_idx_plus_1 = cum_counts[idx]
        cum_counts[idx] -= 1
        result[result_idx_plus_1 - 1] = val

    return result




# TESTS

intsActual = counting_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert counting_sort([]) == []
assert counting_sort([2]) == [2]
