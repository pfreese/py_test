from functools import reduce

test_ls = [1, 1, 3, 4, 9, 10]

## REDUCE
def reduce_add(lst):
    return reduce(lambda x, y: x + y, lst, 0)


def reduce_mult(lst):
    return reduce(lambda x, y: x * y, lst, 1)


def reduce_concat(lst):
    return reduce(lambda x, y: str(x) + "_" + str(y), lst)


# Tests for REDUCE
assert reduce_add(test_ls) == sum(test_ls)
assert reduce_add([]) == 0

assert reduce_mult(test_ls) == 1080

assert reduce_concat(test_ls) == "1_1_3_4_9_10"


### MAP
def map_double(lst):
    return list(map(lambda x: 2 * x, lst))


assert map_double(test_ls) == [2, 2, 6, 8, 18, 20]


### FILTER
def filter_even(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

assert filter_even(test_ls) == [4, 10]
