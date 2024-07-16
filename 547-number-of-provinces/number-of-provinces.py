class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        g = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    g[i].append(j)
        
        visited = set()
        cnt = 0
        def dfs(node):
            for i in g[node]:
                if i not in visited:
                    visited.add(i)
                    dfs(i)
        
        for node in g:
            if node not in visited:
                cnt += 1
                visited.add(node)
                dfs(node)
        
        return cnt
                