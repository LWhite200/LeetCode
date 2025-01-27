" We use the solution in largest rectangle in hostogram "
" We traverse the 2D arraay and we store the current maximum height of each column "
" Proud I came up with this on my own "

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        maxRect = 0
        dp = [0] * cols

        def LRH(heights: List[int]):
            n = len(heights)
            stack = []
            idx = []
            maxArea = 0
            for i, h in enumerate(heights):
                heightStart = i
                while stack and stack[-1] > h:
                    h2 = stack.pop()
                    i2 = idx.pop()
                    maxArea = max(maxArea, h2 * (i - i2)) 
                    heightStart = i2  
                
                stack.append(h)
                idx.append(heightStart)
            for h in stack:
                i = idx.pop(0)
                maxArea = max(maxArea, h * (n - i)) 
            return maxArea
        # ---------------------------------------------------

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    dp[j] += 1
                else:
                    dp[j] = 0

            maxRect = max(maxRect, LRH(dp))

        
        return maxRect


" Even more efficient solution "
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        maxRect = 0
        dp = [0] * cols
        stack = []

        for i in range(rows):
            stack = []
            for j in range(cols):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0

                while stack and dp[stack[-1]] > dp[j]:
                    h = dp[stack.pop()] 
                    width = j if not stack else j - stack[-1] - 1
                    maxRect = max(maxRect, h * width)
                stack.append(j)

            while stack:
                h = dp[stack.pop()]
                width = cols if not stack else cols - stack[-1] - 1
                maxRect = max(maxRect, h * width)

        return maxRect