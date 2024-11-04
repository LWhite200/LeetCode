"So this is a basic back-tracking solution that revisits the same thing position as "
"Each number in the candidates list can be used multiple times"

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(sumTotal, cur, prevList):
            if sumTotal == target:
                res.append(prevList.copy())
                return
            elif sumTotal > target or cur >= len(candidates):
                return 
            
            prevList.append(candidates[cur])
            backtrack(sumTotal + candidates[cur], cur, prevList)
            
            prevList.pop()
            backtrack(sumTotal, cur + 1, prevList)
            
        backtrack(0,0,[])
        return res