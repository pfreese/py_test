def append_strs_efficient(x, y):


assert append_strs_efficient("abcd", "efg") == "abcdefg"


def str_contains_substr(str, substr):


assert str_contains_substr("abcdef", "abc")
assert str_contains_substr("abcdef", "de")
assert not str_contains_substr("abcdef", "efg")


def str_starts_with(str, start):


assert str_starts_with("abcdef", "abc")
assert str_starts_with("abcdef", "a")
assert not str_starts_with("abcdef", "aa")


def str_ends_with(str, end):


assert str_ends_with("abcdef", "ef")
assert str_ends_with("abcdef", "f")
assert not str_ends_with("abcdef", "ff")


def char_to_int(char):


assert char_to_int("d") == 100
assert char_to_int("c") == 99


def int_to_char(int):


assert int_to_char(100) == "d"
assert int_to_char(99) == "c"


def str_is_upper(str):


assert str_is_upper("ABCC")
assert not str_is_upper("AbCC")


def str_is_lower(str):


assert str_is_lower("abc")
assert not str_is_lower("aaA")


def str_to_upper(str):

def str_to_lower(str):



assert str_to_upper("abc") == "ABC"
assert str_to_lower("ABcD") == "abcd"
