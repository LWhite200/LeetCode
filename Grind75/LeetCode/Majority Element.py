class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}  # Use a dictionary to store counts
        
        for n in nums:
            if n in count_dict:
                count_dict[n] += 1
            else:
                count_dict[n] = 1
        
        # Return the element with the maximum count
        return max(count_dict, key=count_dict.get)
