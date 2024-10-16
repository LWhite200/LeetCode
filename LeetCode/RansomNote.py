class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rNote = {}
        maga = {}
        
        if len(magazine) < len(ransomNote):
            return False
        
        for c in ransomNote:
            rNote[c] = rNote.get(c, 0) + 1
            
        for c in magazine:
            maga[c] = maga.get(c, 0) + 1
            
        for c in rNote:
            if maga.get(c, 0) < rNote[c]:
                return False
        
        return True
    
    
    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga = {}
        
        # Count characters in magazine
        for c in magazine:
            maga[c] = maga.get(c, 0) + 1
            
        # Check if ransomNote can be constructed
        for c in ransomNote:
            if maga.get(c, 0) == 0:  # If c is not available or exhausted
                return False
            maga[c] -= 1  # Use one instance of character
        
        return True

