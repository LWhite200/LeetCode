class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        w = len(obstacleGrid)
        h = len(obstacleGrid[0])

        dp = [0] * h
        dp[h - 1] = 1

        for i in range(w -1, -1, -1):
            for j in range(h - 1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j + 1 < h : # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    dp[j] += dp[j + 1]

        return dp[0]