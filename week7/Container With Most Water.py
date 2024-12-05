class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        maxWater = 0
        
        
        while l < r:
            tall = min(height[r], height[l])
            distance = r - l
            
            maxWater = max(maxWater, distance * tall)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
                
        return maxWater