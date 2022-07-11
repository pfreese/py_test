###  45654

# n_digits = 5
#### 43210

def get_n_digits(num):
    n_digits = 0
    while True:
        if num + 1 <= int(10 ** n_digits):
            return n_digits
        n_digits += 1

def get_digit(num, pow_of_10):
    num_wo_preceding = num % (pow_of_10 * 10)
    result = int((num_wo_preceding - (num_wo_preceding % pow_of_10))/pow_of_10)
    assert result in list(range(10))
    return result

def check_palindrome(num):
    n_digits = get_n_digits(num)
    for exponent in range(n_digits):
        right_digit = get_digit(num, 10 ** exponent)
        left_digit = get_digit(num, 10 ** (n_digits - exponent - 1))
        if right_digit != left_digit:
            return False
    return True

assert check_palindrome(4)
assert check_palindrome(44)
assert check_palindrome(45654)
assert check_palindrome(1331)

assert not check_palindrome(1336)
assert not check_palindrome(136)
