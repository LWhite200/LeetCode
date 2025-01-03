class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        res = []
        
        # w is the s we are changing
        def search(index, w):
            
            if index > 0:
                return True
            
            for i in range(len(w) - 1, -1, -1):
                if w[i:] in wordDict:
                    res.add(w[i:])
                    if search(i, w[:i]) == False:
                        res.pop()
                    else:
                        return True
            
        reachedEnd = search(len(s), s)
        retLen = sum(len(r) for r in res)
        
        return reachedEnd and retLen == len(s)