class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Put a list of all nodes and their neighbors
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        # Keep track of the amount of neighbors of each node
        # and also which nodes are leaves
        edge_cnt = {}
        leaves = deque()
        for src, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edge_cnt[src] = len(neighbors)
            
        # BFS on the leaves nodes until 1 or 2 middle nodes are left
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)