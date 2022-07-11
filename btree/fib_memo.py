class Solution:

    def __init__(self):
        #self.memo = {1: 1, 2: 1}
        self.memo = {}

    def fib(self, n):
        if n <= 2:
            return 1

        if n in self.memo:
            return self.memo[n]

        result = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = result

        return result

sol = Solution()
assert sol.fib(1) == 1
assert sol.fib(2) == 1
assert sol.fib(3) == 2
assert sol.fib(4) == 3
assert sol.fib(5) == 5
assert sol.fib(6) == 8
assert sol.fib(7) == 13
