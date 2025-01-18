" DP bottom-up "
" very weird as you most check if values in range can also reach end "

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [float('inf')] * len(nums) # since we want to find minimum steps
        dp[-1] = 0 # no steps needed

        for i in range(len(nums) - 2, -1, -1):

            # The max reach
            max_reach = min(i + nums[i], len(nums) - 1)

            # iterate the steps it has to see if it can go 
            for j in range(i + 1, max_reach + 1):
                dp[i] = min(dp[i], 1 + dp[j])

        return dp[0] 
