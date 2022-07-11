import sort_utils


def countingSort(array):
    n = len(array)
    if n < 2:
        return array
    min_val = min(array)
    max_val = max(array)

    range_vals = max_val - min_val
    if range_vals == 0:
        return array

    # range_vals + 1 counts.
    counts = [0 for _ in range(range_vals + 1)]

    for val in array:
        idx = val - min_val
        counts[idx] += 1
    # Get cumulative counts.
    cum_counts = counts
    for i in range(1, range_vals + 1):
        cum_counts[i] = cum_counts[i] + cum_counts[i-1]

    result = [None for _ in range(n)]
    for val in array[::-1]:
        counts_idx = val - min_val
        result_idx_plus_1 = cum_counts[counts_idx]
        cum_counts[counts_idx] -= 1
        result[result_idx_plus_1 - 1] = val
    return result



# TESTS

intsActual = countingSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert countingSort([]) == []
assert countingSort([2]) == [2]
