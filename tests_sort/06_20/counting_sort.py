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

    # counts.
    counts = [0 for _ in range(range_vals + 1)]
    for val in array:
        idx = val - min_val
        counts[idx] += 1
    # Get cumulative counts.
    cumul_counts = counts
    for i in range(1, len(counts)):
        cumul_counts[i] = cumul_counts[i] + cumul_counts[i - 1]

    # Assemble result.
    result = [None for _ in range(n)]
    for val in array[::-1]:
        idx = val - min_val
        result_idx_plus_1 = cumul_counts[idx]
        cumul_counts[idx] -= 1
        result[result_idx_plus_1 - 1] = val

    return result



# TESTS

intsActual = countingSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert countingSort([]) == []
assert countingSort([2]) == [2]
