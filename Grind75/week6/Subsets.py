# Very Basic Backtrack

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(curSet, index):
            if index >= len(nums):
                res.append(curSet)
                return
            
            backtrack(curSet + [nums[index]], index + 1)
            backtrack(curSet, index + 1)
            
        backtrack([], 0)
        return res