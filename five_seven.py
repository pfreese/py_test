import random
from collections import defaultdict
import pprint

def rand_5():
    return random.randrange(5)


def rand_7():
    v1 = rand_5()
    v2 = rand_5()
# r_25 is random from [0, 24]
    r_25 = (v1 * 5) + v2
    if (r_25 >= 21):
        return rand_7()
    else:
        return (r_25 % 7) + 1

#for i in range(10):
#    print(rand_5())


rand_7_dict = defaultdict(int)

for i in range(100000):
    rand_7_dict[rand_7()] += 1

n_total_counts = sum(rand_7_dict.values())

rand_7_freq = {}
for key, count in rand_7_dict.items():
    rand_7_freq[key] = count/n_total_counts

#print(rand_7_dict)
pprint.pprint(rand_7_dict)
pprint.pprint(rand_7_freq)
