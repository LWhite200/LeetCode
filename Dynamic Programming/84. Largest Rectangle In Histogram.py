" This is pain, needed for question 85 "
" maintain index and height in a stack as long as the current is greater than the last "

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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

        # for loops go in fifo, unlike stacks!!!!!!!!!!
        for h in stack:
            i = idx.pop(0)
            maxArea = max(maxArea, h * (n - i)) 

        return maxArea
