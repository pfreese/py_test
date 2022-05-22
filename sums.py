

def swap(lst):
    if len(lst) < 2:
        return lst
    first = lst[0]
    last = lst[-1]
    return [last] + lst[1:-1] + [first]

print(swap([12, 35, 9, 56, 24]))
print(swap([1, 2, 3]))
