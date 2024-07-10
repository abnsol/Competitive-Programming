class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = defaultdict(list)

        def finddistance(x1,x2,y1,y2):
            return sqrt((x2 - x1)**2 + (y2 - y1)**2)

        for i in range(len(bombs)):
            x1,y1,r1 = bombs[i]
            for j in range(i + 1,len(bombs)):
                x2,y2,r2 = bombs[j]
                print(x2,y2,r2)
                distance = finddistance(x1,x2,y1,y2)
                if distance <= r1:
                    g[i].append(j)
                if distance <= r2:
                    g[j].append(i)
        
        def dfs(node,visited):
            count = 1
            visited.add(node)
            for i in g[node]:
                if i not in visited:
                    count += dfs(i,visited)
            return count
        
        _max = 1
        for i in range(len(bombs)):
            _max = max(_max,dfs(i,set()))
        
        return _max


                