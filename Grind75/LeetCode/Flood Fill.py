class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        cache = set()
        prevColor = image[sr][sc]
        
        def dfs(r: int, c: int):
            if not (0 <= r < rows and 0 <= c < cols) or image[r][c] != prevColor or (r, c) in cache:
                return
            image[r][c] = color
            cache.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        if prevColor != color:  # Avoids infinite loop 
            dfs(sr, sc)
            
        return image

    