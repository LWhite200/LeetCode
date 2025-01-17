from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for n in prices:
            if n < lowest:
                lowest = n
            res = max(res, n - lowest)
            
        return res


if __name__ == "__main__":
    # Instantiate the class
    solution = Solution()
    # Call the method with test parameters
    result = solution.maxProfit([7,1,5,3,6,4])
    print(result)
    
    # Pause the program
    input("Press Enter to close...")