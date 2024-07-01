class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        
        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            
            for i in g[node]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
            
        return False

'''
0 : 1
1 : 2
2 : 0
'''