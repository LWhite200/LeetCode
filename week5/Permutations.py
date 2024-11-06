"Recusive back-tracking by seperating letters and combinations"

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:]) # recursion to get all versions
        
        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                res.append(perm_copy)
        return res