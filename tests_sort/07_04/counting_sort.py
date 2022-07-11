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
    for v in array:
        counts_idx = v - min_val
        counts[counts_idx] += 1

    cumul_counts = counts
    for i in range(1, val_range + 1):
        cumul_counts[i] = cumul_counts[i] + cumul_counts[i-1]

    result = [None for _ in range(n)]
    for v in array[::-1]:
        counts_idx = v - min_val
        result_idx_plus_1 = cumul_counts[counts_idx]
        cumul_counts[counts_idx] -= 1
        result[result_idx_plus_1 - 1] = v
    return result




# TESTS

intsActual = counting_sort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert counting_sort([]) == []
assert counting_sort([2]) == [2]
