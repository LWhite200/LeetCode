class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        l, r = 2, 3
        
        for i in range(4, n + 1):
            t = l + r
            l = r
            r = t
            
        return r