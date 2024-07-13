class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int: 
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        
        def dfs(node,parent):
            time = 0

            for child in g[node]:
                if child == parent:
                    continue
                temp = dfs(child,node)
                if temp or hasApple[child]:
                    time += 2 + temp
            
            return time
        return dfs(0,-1)

        