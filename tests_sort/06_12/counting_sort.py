import sort_utils


# Want to create buckets

def countingSort(array):
    n = len(array)
    if n < 2:
        return array

    max_val = max(array)
    min_val = min(array)
    val_range = max_val - min_val
    counts = [0 for _ in range(val_range + 1)]

    for val in array:
        idx = val - min_val
        counts[idx] += 1

    cumul_counts = counts
    for i in range(1, n):
        cumul_counts[i] = cumul_counts[i] + cumul_counts[i-1]

    result = [None for _ in range(n)]

    for val in array[::-1]:
        idx = val - min_val
        result_idx = cumul_counts[idx] - 1
        cumul_counts[idx] -= 1
        assert result_idx >= 0
        assert result_idx < n
        assert result[result_idx] is None
        result[result_idx] = val

    return result



# TESTS

intsActual = countingSort(sort_utils.unsortedInts)
assert intsActual == sort_utils.sortedInts
print(intsActual)

assert countingSort([]) == []
assert countingSort([2]) == [2]
