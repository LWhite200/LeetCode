class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter= {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        res = []
        
        def backtrack(cur, idx):
            if idx >= len(digits):
                res.append(cur)
                return
            
            for c in letter[digits[idx]]:
                backtrack(cur + c, idx + 1)
           
        if digits:
            backtrack("", 0)
        
        return res