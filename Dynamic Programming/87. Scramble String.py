" Variation of anagram and also some backtracking "

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = {}

        # recursive algorithm
        def splice(s1, s2):
            if (s1, s2) in dp:
                return dp[(s1, s2)]
            if not sorted(s1) == sorted(s2): # make sure they are anagrams
                return False
            if len(s1) == 1: # since anagrams
                return True

            for i in range(1, len(s1)):

                # if any combination is good
                if splice(s1[:i], s2[-i:]) and splice(s1[i:], s2[:-i])    or    splice(s1[:i], s2[:i]) and splice(s1[i:], s2[i:]):
                    dp[(s1, s2)] = True
                    return True
            dp[(s1, s2)] = False
            return False

        
        
        return splice(s1, s2)
        
