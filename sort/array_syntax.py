from functools import reduce

test_ls = [1, 1, 3, 4, 9, 10]

## REDUCE
def reduce_add(lst):
    result = reduce(lambda x, y: x + y, lst, 0)
    return result

def reduce_mult(lst):
    result = reduce(lambda x, y: x * y, lst)
    return result

def reduce_concat(lst):
    result = reduce(lambda x, y: str(x) + "_" + str(y), lst)
    return result

# Tests for REDUCE
assert reduce_add(test_ls) == sum(test_ls)
assert reduce_add([]) == 0

assert reduce_mult(test_ls) == 1080

assert reduce_concat(test_ls) == "1_1_3_4_9_10"


### MAP
def map_double(lst):
    result = list(map(lambda x: 2*x, lst))
    return result

assert map_double(test_ls) == [2, 2, 6, 8, 18, 20]


### FILTER
def filter_even(lst):
    return list(filter(lambda x: x % 2 == 0, test_ls))

assert filter_even(test_ls) == [4, 10]

# LOOP LOGIC.
# CBP (continue; break; pass)
# (Customs and Border Patrol)

# Print 1-10 except for 5.
result = []
for i in range(10):
    if i == 5:
        continue
    result.append(i)
assert result == [0, 1, 2, 3, 4, 6, 7, 8, 9]

# Two loops each 0, 1, 2; break inner loop once it hits 1.
result = []
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        result.append(f"i={i}, j={j}")
assert result == ['i=0, j=0', 'i=1, j=0', 'i=2, j=0']


# Pass: skip over x=5 but print all 0-10.
result = []
for i in range(10):
    if i == 5:
        pass
    result.append(i)
assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
