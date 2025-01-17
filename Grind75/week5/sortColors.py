"This solution is stupid and basic"
"I might try quick-sort"

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        colors = [0, 0, 0]
        
        for n in nums:
            colors[n] += 1
        
        colPoint = 0
        for i in range(len(nums)):
            while colors[colPoint] == 0:
                colPoint += 1
            nums[i] = colPoint
            colors[colPoint] -= 1