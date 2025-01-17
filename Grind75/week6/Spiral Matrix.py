class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        up, down = 0, len(matrix)
        
        while left < right and up < down:
            for i in range(left, right):
                res.append(matrix[up][i])
            up += 1
                
            for i in range(up, down):
                res.append(matrix[i][right - 1])
            right -= 1
            
            if not (left < right and up < down): 
                break
                
            for c in range(right - 1, left - 1, -1):
                res.append(matrix[down - 1][c]) 
            down -= 1
                
            for c in range(down - 1, up - 1, -1):
                res.append(matrix[c][left]) 
            left += 1
                
        return res