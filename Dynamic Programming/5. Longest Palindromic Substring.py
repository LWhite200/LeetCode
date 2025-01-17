" Familiar, have done this in class "
" dp at it's finest I guess "
" Start at each character and try to expand outwards, do twice for even-sized"

class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        rLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > rLen: # Must add 1 as index 0 messes things up
                    res = s[l:r+1]
                    rLen = r-l
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > rLen:
                    res = s[l:r+1]
                    rLen = r-l
                l -= 1
                r += 1
        
        return res