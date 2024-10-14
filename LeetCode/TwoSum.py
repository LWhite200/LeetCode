from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in cache:
                return [cache[diff], i]
            cache[n] = i

if __name__ == "__main__":
    # Instantiate the class
    solution = Solution()
    # Call the method with test parameters
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)
    
    # Pause the program
    input("Press Enter to close...")
