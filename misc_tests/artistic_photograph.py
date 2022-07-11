from typing import List
# Write any import statements here
from collections import defaultdict

def getMinProblemCount(S: List[int]) -> int:
  # Write your code here
  all_even = all([x % 2 == 0 for x in S])
  print(all_even)
  max_val = max(S)
  if all_even:
      return int(max_val / 2)
  ## Max val is 4 -> 2. Two 2's plus one 1.
  ## Max val is 5.
  return (max_val // 2) + 1

print(getMinProblemCount([2, 4, 6, 8]))
