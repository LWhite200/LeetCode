class Solution:
    def reverse(self, x: int) -> int:
        
        neg = False
        if x < 0:
            neg = True
            x *= -1

        Stack = []

        tX = str(x)

        for c in tX:
            Stack.append(c)
        
        res = 0
        idx = 1
        while Stack:
            c = Stack.pop()  
            res = res * 10 + int(c)  
        
        if neg:
            res *= -1
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res
