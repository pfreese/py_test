import sort_utils

def pow_of_10_digit(x, pow_of_10):
    x_and_after = x % (10 * pow_of_10)
    x_time_pow_of_10 = x_and_after - (x_and_after % pow_of_10)
    result = x_time_pow_of_10 / pow_of_10
    assert result in list(range(10))
    return int(result)


def sort_by_pow_of_10_digit(array, pow_of_10):

    num_and_pow_of_10s = [(x, pow_of_10_digit(x, pow_of_10)) for x in array]
    # Counting sort.
    counts = [0 for _ in range(10)]
    for _, digit in num_and_pow_of_10s:
        counts[digit] += 1
    # Get cumul. counts.
    cumul_counts = counts
    for i in range(1, len(cumul_counts)):
        cumul_counts[i] = cumul_counts[i] + cumul_counts[i-1]
    # Initialize result.
    array_sorted_by_digit = [None for _ in range(len(array))]
    for x, digit in num_and_pow_of_10s[::-1]:
        pos_plus_1 = cumul_counts[digit]
        cumul_counts[digit] -= 1
        array_sorted_by_digit[pos_plus_1-1] = x
    # Check.
    assert not any([x is None for x in array_sorted_by_digit])
    return array_sorted_by_digit

def get_n_digits(x):
    if x == 0:
        return 1
    n_digits = 0
    while x > 0:
        n_digits += 1
        x = x // 10
    return n_digits


def radixSort(array):
    if len(array) < 2:
        return array
    # Get max. number of digits.
    max_n_digits = max([get_n_digits(x) for x in array])

    # Iterate through digits from least signif. to most signif.
    for n_digits in range(max_n_digits):
        # pow_of_10 is 1, 10, 100, ...
        pow_of_10 = int(10 ** n_digits)

        # Sort according to digit at power of 10 position.
        array = sort_by_pow_of_10_digit(array, pow_of_10)

    return array


# TESTS

actual = radixSort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radixSort([]) == []
assert radixSort([2000]) == [2000]
