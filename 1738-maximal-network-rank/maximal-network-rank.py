class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in roads:
            g[u].add(v)
            g[v].add(u)
        
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                val = len(g[i]) + len(g[j])
                if j in g[i]:
                    val -= 1
                ans = max(ans, val)
        
        return ans
