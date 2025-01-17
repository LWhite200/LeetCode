class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        
        if not root:
            return []
        
        q.append(root)
        
        while q:
            right = float('-inf')
            for i in range(len(q)):
                cur = q.popleft()
                
                if(cur):
                    right = cur.val
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(right)
        return res