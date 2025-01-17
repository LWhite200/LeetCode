" So We basically just use binary sort "
" But we need to make sure that we adjust "
" and find the segment containing target that "
" is in order from least to greatest. "

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]: 
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: 
                if nums[mid] < target <= nums[right]: 
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1 
