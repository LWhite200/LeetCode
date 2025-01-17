" I've basically had this memorized as I have done this one so many times "
" Basic dp, move forward if match and no *, if *, go try going forward with reuse or not reuse "

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = {}

        def dfs(i, j):

            # if end or already know cache
            if j == n:
                return i == m
            if (i, j) in cache:
                return cache[(i, j)]

            # if the current par is adequit
            match = i < m and (s[i] == p[j] or p[j] == ".")

            # if the next space is repeat, find adequate solution if possible, the "j + 2" as you skip star
            if j + 1 < n and p[j+1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or match and dfs(i+ 1, j)
                return cache[(i, j)]

            # If there is a match, we delve deeper
            if match:
                cache[(i, j)] = dfs(i+1,j+1)
                return cache[(i,j)]

            return False
        return dfs(0,0)