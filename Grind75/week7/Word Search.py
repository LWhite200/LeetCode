class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        
        visit = set()
        
        def search(x, y, index):
            if index == len(word):  
                return True
            
            if (x < 0 or x >= row or y < 0 or y >= col or 
                (x, y) in visit or board[x][y] != word[index]):
                return False
            
            visit.add((x, y))
            
            if (search(x + 1, y, index + 1) or 
                search(x - 1, y, index + 1) or 
                search(x, y + 1, index + 1) or 
                search(x, y - 1, index + 1)):
                return True
            
            visit.remove((x, y))
            
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if search(i, j, 0):
                        return True
                    
        return False
