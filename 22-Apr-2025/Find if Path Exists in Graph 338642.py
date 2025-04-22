# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(list)
        for i,j in edges:
            g[i].append(j)
            g[j].append(i)
        
        ans = [False]
        visited = set()
        def dfs(vertex):
            if vertex == destination:
                ans[0] = True
                return
            
            visited.add(vertex)
            for child in g[vertex]:
                if not ans[0] and child not in visited:
                    dfs(child)
        
        dfs(source)
        return ans[0]
                
            
            


            
        