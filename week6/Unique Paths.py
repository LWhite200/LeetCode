class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [1] * n
        
        for i in range(m - 1):
            for j in range(n - 2, -1, -1):
                DP[j] = DP[j] + DP[j + 1]
                    
        return DP[0]