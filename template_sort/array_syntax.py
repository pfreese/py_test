test_ls = [1, 1, 3, 4, 9, 10]

## REDUCE
def reduce_add(lst):


def reduce_mult(lst):


def reduce_concat(lst):


# Tests for REDUCE
assert reduce_add(test_ls) == sum(test_ls)
assert reduce_add([]) == 0

assert reduce_mult(test_ls) == 1080

assert reduce_concat(test_ls) == "1_1_3_4_9_10"


### MAP
def map_double(lst):


assert map_double(test_ls) == [2, 2, 6, 8, 18, 20]


### FILTER
def filter_even(lst):


assert filter_even(test_ls) == [4, 10]
