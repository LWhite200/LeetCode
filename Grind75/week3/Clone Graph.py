from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
          
        cloneMap = {}

        def dfs(node):
            
            if node in cloneMap:
                return cloneMap[node]

            copy = Node(node.val)
            cloneMap[node] = copy
            
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
            

        return dfs(node) if node else None