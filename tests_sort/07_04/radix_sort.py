import sort_utils

def get_pow_10_digit(val, pow_10):
    # val = 3245
    # pow_10 = 10

    # val_at_after = 45
    val_at_after = val % (10 * pow_10)
    # val_after = 5
    val_after = val_at_after % pow_10

    # result = (45 - 5) / 10 = 4
    result = int((val_at_after - val_after) / pow_10)
    assert result in list(range(10))
    return result


def counting_sort_on_pow_10(array, pow_10):
    # Get digit at pow_10 position for each number.
    pow_10_digits = [(x, get_pow_10_digit(x, pow_10)) for x in array]

    counts = [0 for _ in range(10)]
    for _, digit in pow_10_digits:
        counts[digit] += 1
    cum_counts = counts
    for i in range(1, 10):
        cum_counts[i] = cum_counts[i] + cum_counts[i-1]

    result = [None for _ in array]
    for v, digit in pow_10_digits[::-1]:
        result_idx_plus_1 = cum_counts[digit]
        cum_counts[digit] -= 1
        result[result_idx_plus_1 - 1] = v
    return result


def get_n_digits(x):
    if x == 0:
        return 1
    n_digits = 1
    while True:
        if x + 1 <= int(10 ** n_digits):
            return n_digits
        n_digits += 1


def radix_sort(array):
    if len(array) < 2:
        return array
    max_n_digits = max([get_n_digits(x) for x in array])

    for digit_idx in range(max_n_digits):
        # pow_10 is 1, 10, 100, ...
        pow_10 = int(10 ** digit_idx)
        array = counting_sort_on_pow_10(array, pow_10)
    return array


# TESTS

actual = radix_sort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radix_sort([]) == []
assert radix_sort([2000]) == [2000]
