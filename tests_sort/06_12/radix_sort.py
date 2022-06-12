import sort_utils

def n_digits(x):
    n_dig = 1
    while True:
        if x + 1 <= int(10 ** n_dig):
            return n_dig
        n_dig += 1

def extract_pow_10_digit(x, digit_to_pow_10):
    x_at_after_digit = x % (10 * digit_to_pow_10)
    x_after_digit = x_at_after_digit % digit_to_pow_10
    digit = int((x_at_after_digit - x_after_digit) / digit_to_pow_10)
    assert digit in list(range(10))
    return digit

def sort_by_digit_pow_10(array, digit_to_pow_10):
    n = len(array)
    array_w_digits = [(x, extract_pow_10_digit(x, digit_to_pow_10)) for x in array]
    # Counting sort based on the digits.
    counts = [0 for _ in range(10)]
    for _, digit in array_w_digits:
        counts[digit] += 1
    # Get cumulative counts.
    cumul_counts = counts
    for i in range(1, len(cumul_counts)):
        cumul_counts[i] = cumul_counts[i] + cumul_counts[i - 1]

    result = [None for _ in range(n)]

    for val, digit in array_w_digits[::-1]:
        result_idx = cumul_counts[digit] - 1
        cumul_counts[digit] -= 1
        assert result_idx >= 0
        assert result_idx < n
        assert result[result_idx] is None
        result[result_idx] = val
    return result

def radixSort(array):
    n = len(array)
    if n < 2:
        return array

    # Get max number of digis.
    max_n_digits = max([n_digits(x) for x in array])

    # Need to sort by 1s, then 10s, etc.
    for digit_n in range(max_n_digits):
        digit_to_pow_10 = int(10 ** digit_n)

        array = sort_by_digit_pow_10(array, digit_to_pow_10)

    return array


# TESTS

actual = radixSort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radixSort([]) == []
assert radixSort([2000]) == [2000]
