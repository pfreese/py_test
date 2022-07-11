import sort_utils

def get_pow_10_digit(x, pow_10):
    x_sans_gr_pow_10 = x % int(10 * pow_10)
    x_remainder = x_sans_gr_pow_10 - (x_sans_gr_pow_10 % pow_10)
    result = int(x_remainder / pow_10)
    assert result in range(10)
    return result

def counting_sort_pow_10(array, pow_10):

    val_pow_10_digits = [(x, get_pow_10_digit(x, pow_10)) for x in array]
    counts = [0 for _ in range(10)]
    for val, val_digit in val_pow_10_digits:
        counts[val_digit] += 1
    # Get cumulative counts.
    cumul_counts = counts
    for i in range(1, 10):
        cumul_counts[i] = cumul_counts[i] + cumul_counts[i-1]
    result = [None for _ in range(len(array))]
    for val, val_digit in val_pow_10_digits[::-1]:
        result_idx_plus_1 = cumul_counts[val_digit]
        assert result[result_idx_plus_1-1] is None
        result[result_idx_plus_1-1] = val
        cumul_counts[val_digit] -= 1
    assert not any([x is None for x in result])
    return result



def get_n_digits(val):
    n_digits = 1
    while True:
        if val + 1 <= 10 ** n_digits:
            return n_digits
        n_digits += 1

def radixSort(array):
    n = len(array)
    if n < 2:
        return array

    # Get the max. number of digits.
    max_n_digits = max([get_n_digits(x) for x in array])

    # Sort from last to first digit.
    for n_digits in range(max_n_digits):
        # pow_10 is 1, 10, 100, ...
        pow_10 = int(10 ** n_digits)

        array = counting_sort_pow_10(array, pow_10)

    return array


# TESTS

actual = radixSort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radixSort([]) == []
assert radixSort([2000]) == [2000]
