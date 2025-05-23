# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        result = True
        for node in color:
            if color[node] == -1:
                color[node] = 0
                result = result and self.dfs(graph,node,color)
            
        return result
    
    def dfs(self,graph,node,color):
        temp = True
        for child in graph[node]:
            if color[child] == -1:
                color[child] = 1 - color[node]
                temp = temp and self.dfs(graph,child,color)
            elif color[node] == color[child]:
                return False
        
        return temp

        