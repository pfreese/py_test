def find_132(array):
    if len(array) < 3:
        return False
    min_1 = float('inf')
    max_2 = float('-inf')
    for i, val in enumerate(array):
        if i == 0:
            min_1 = val
        else:
            if val > min_1 and val < max_2:
                print(min_1)
                print(max_2)
                print(val)
                return True
            if val < min_1:
                min_1 = val
            elif val > min_1 and val > max_2:
                max_2 = val
    return False

print(find_132([1,0,1,-4,-3]))
