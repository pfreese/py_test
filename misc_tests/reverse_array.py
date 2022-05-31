def find_132(array):
    queue = []
    minVal = array[0]
    for v in array[1:]:
        while queue and v >= queue[-1][0]:
            queue.pop()
        if queue and v < queue[-1][1]:
            return True
        queue.append((v, minVal))
        minVal = min(minVal, v)
    return False

print(find_132([1,0,1,-4,-3]))

# 5 2
