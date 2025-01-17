class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []

        vals = []
        q = deque()
        q.append(root)
        
        while q:
            cur = q.popleft()
            vals.append(cur.val)
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        
        vals.sort()
        
        return vals[k - 1]