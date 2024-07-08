class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node):
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    if not dfs(neighbor):
                        return False
                elif color[node] == color[neighbor]:
                    return False
                                
            return True

        n = len(graph)
        color = [-1 for _ in range(n)]
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False
        
        return True