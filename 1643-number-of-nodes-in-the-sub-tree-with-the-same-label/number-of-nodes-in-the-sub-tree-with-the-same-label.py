class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        res = [0] * n
        visited = set()
        def dfs(node,hashmap):
            if node in visited:
                return hashmap

            hashmap[labels[node]] = hashmap.get(labels[node],0) + 1  
            visited.add(node)
            for neighbor in g[node]:
                ans = dfs(neighbor,{})
                for keys in ans:
                    hashmap[keys] = hashmap.get(keys,0) +  ans[keys]
            
            res[node] += hashmap[labels[node]]
            return hashmap
        
        dfs(0,{})
        return res
        