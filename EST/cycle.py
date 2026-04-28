from collections import deque

class Solution:
    def isCyclic(self, V, adj):
        real_adj = [[] for _ in range(V)]
        in_degree = [0] * V
        
        for u, v in adj:
            real_adj[u].append(v)
            in_degree[v] += 1
                t
       
        queue = deque([i for i in range(V) if in_degree[i] == 0])
        count = 0
        

        while queue:
            u = queue.popleft()
            count += 1
            
            for v in real_adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
       
        return count != V
