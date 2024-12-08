class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []
        
        res = []
        pAna = {}
        curWin = {}
        
        # -------------------------------
        for c in p:
            pAna[c] = pAna.get(c, 0) + 1
        
        for i in range(len(p)):
            curWin[s[i]] = curWin.get(s[i], 0) + 1
        
        if curWin == pAna:
            res.append(0)
        
        # ---------------------------------
        for i in range(1, len(s) - len(p) + 1):
            left_char = s[i - 1]
            curWin[left_char] -= 1
            if curWin[left_char] == 0:
                del curWin[left_char]
            
            right_char = s[i + len(p) - 1]
            curWin[right_char] = curWin.get(right_char, 0) + 1
            
            if curWin == pAna:
                res.append(i)
        
        return res
