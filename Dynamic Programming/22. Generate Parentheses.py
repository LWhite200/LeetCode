" So We are given the amount of spaces n*2 which should be permutations of open closed braces "
" Very simple, just make sure the amount of each type of brace never becomes more than half "

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cache = []
        
        def dfs(i, cur, Opn, Clsd):
            if i == n*2:
                cache.append(cur)
                return

            if Opn + 1 <= n and Clsd <= n:
                dfs(i + 1, cur + "(", Opn + 1, Clsd)

            if Opn > Clsd and Opn <= n and Clsd + 1 <= n:
                dfs(i + 1, cur + ")", Opn, Clsd + 1)


        dfs(0, "", 0, 0)
        return cache
                