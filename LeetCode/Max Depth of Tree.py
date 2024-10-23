class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque()
        if root:
            q.append(root)
            
        while q:
            val = []
            for n in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1
        
        return res