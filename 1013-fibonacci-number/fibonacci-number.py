class Solution:
    def fib(self, n: int) -> int:
        maps = {0:0,1:1}
        def recurse(n):
            if n <= 1:
                return n
            
            if n not in maps:
                maps[n] = recurse(n - 1) + recurse(n - 2)
                return maps[n]
            else:
                return maps[n]
        
        return recurse(n)
            