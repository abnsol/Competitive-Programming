class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a,b in dislikes:
            g[a].append(b)
            g[b].append(a)               
                
        color = [-1] * n
        visited = set()

        def dfs(node):
            for val in g[node]:
                if color[val - 1] == -1:
                    color[val - 1] = 1 - color[node - 1]
                    if not dfs(val):
                        return False
                    visited.add(val)

                elif color[node - 1] == color[val - 1]:
                    return False 
            
            return True

        for keys in g:
            if keys not in visited:
                color[keys - 1] = 0
                if not dfs(keys):
                    return False
        
        return True