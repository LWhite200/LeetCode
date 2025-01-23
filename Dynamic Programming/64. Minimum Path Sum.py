" Simple bottom-up DP, nothing else to it "

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        for i in range(r - 1, -1, -1):
            for j in range(c -1, -1, -1):
                if i < r-1 and j < c-1:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
                elif i < r-1:
                    grid[i][j] += grid[i+1][j]
                elif j < c-1:
                    grid[i][j] += grid[i][j + 1]
        return grid[0][0]