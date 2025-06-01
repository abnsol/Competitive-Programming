# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, n):
        if n != self.parents[n]:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]
    
    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)

        if u_parent != v_parent:
            if self.rank[u_parent] > self.rank[v_parent]:
                self.parents[v_parent] = u_parent
            elif self.rank[u_parent] < self.rank[v_parent]:
                self.parents[u_parent] = v_parent
            else:
                self.parents[u_parent] = v_parent
                self.rank[v_parent] += 1
            return False # They are not connected

        return True # They are connected

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n_points = len(points)
        q = [] # To contain the edges sorted increasing order
        heapq.heapify(q)
        for i in range(n_points):
            for j in range(i+1, n_points):
                x1,y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(q, (distance, i, j))
        
        edge_count = 0
        res = 0
        uf = UnionFind(n_points)
        while edge_count < n_points:
            if edge_count == n_points-1:
                break
            curr_dist, point1, point2 = heapq.heappop(q)
            if uf.union(point1, point2):
                continue
            else:
                res+=curr_dist
                edge_count+=1
        
        return res