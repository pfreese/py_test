import sort_utils

def get_digit_i(x, pow_10):
    x_sans_left = x % (10 * pow_10)
    right_of_pow = x_sans_left % pow_10
    result = int((x_sans_left - right_of_pow) / pow_10)
    assert result in list(range(10))
    return result


def sort_on_digit_i(array, digit_i):
    digit_i_pow_10 = int(10 ** digit_i)

    array_digit_i = [(x, get_digit_i(x, digit_i_pow_10)) for x in array]

    counts = [0 for _ in range(10)]
    for _, digit in array_digit_i:
        counts[digit] += 1

    cum_counts = counts
    for i in range(1, 10):
        cum_counts[i] = cum_counts[i] + cum_counts[i-1]

    result = [None for _ in range(len(array_digit_i))]

    for x, digit in array_digit_i[::-1]:
        result_idx_plus_1 = cum_counts[digit]
        cum_counts[digit] -= 1
        result[result_idx_plus_1 - 1] = x
    return result



def n_digits(x):
    if x == 0:
        return 1
    n_dig = 1
    while True:
        if x < int(10 ** n_dig):
            return n_dig
        n_dig += 1

def radix_sort(array):
    if len(array) == 0:
        return []
    max_n_digits = max([n_digits(x) for x in array])

    for digit_i in range(max_n_digits):
        array = sort_on_digit_i(array, digit_i)
    return array


# TESTS

actual = radix_sort(sort_utils.radixInputVals)
print(actual)
assert actual == sort_utils.radixSortedVals


assert radix_sort([]) == []
assert radix_sort([2000]) == [2000]
