" bottom-up dfs "
" We create a goal where the last index had a path reaching the end "
" and we check to see if the next (previous) index can reach it "

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canJumpTo = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= canJumpTo:
                canJumpTo = i
        
        return True if canJumpTo == 0 else False