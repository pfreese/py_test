

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_memoized_helper(n, fib_dict):
    try:
        result = fib_dict[n]
        return result, fib_dict
    except KeyError:
        result_n_minus_1, fib_dict = fib_memoized_helper(n - 1, fib_dict)
        fib_dict[n - 1] = result_n_minus_1

        result_n_minus_2, fib_dict = fib_memoized_helper(n - 2, fib_dict)
        fib_dict[n - 2] = result_n_minus_2

        return result_n_minus_1 + result_n_minus_2, fib_dict

def fib_memoized(n):
    fib_dict = {1: 1, 2: 1}
    result, _ = fib_memoized_helper(n, fib_dict)
    return result

print(fib_memoized(50))

#for i in range(30):
#    print(fib_memoized(i))
