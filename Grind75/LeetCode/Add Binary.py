class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            dA = int(a[i]) if i < len(a) else 0 # if i is inbounds of a's length
            dB = int(b[i]) if i < len(b) else 0
            
            total = dA + dB + carry
            char = str(total % 2) # so % 2 is 0, so the carry is 1 else
            res = char + res
            carry = total // 2 # since 3 // 2 and 2//2 both equal 1
            
        if carry:
            res = "1" + res
        return res