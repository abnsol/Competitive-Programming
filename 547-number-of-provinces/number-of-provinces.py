class UnionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self,child):
        if child == self.parent[child]:
            return child

        self.parent[child] = self.find(self.parent[child])
        return self.parent[child]
    
    def union(self,x,y):
        parentx = self.find(x)
        parenty = self.find(y)
        if parentx != parenty:
            if self.rank[parentx] > self.rank[parenty]:
                self.parent[parenty] = parentx
            elif self.rank[parenty] > self.rank[parentx]:
                self.parent[parentx] = parenty
            else:
                self.parent[parentx] = parenty
                self.rank[parenty] += 1
    
    def isconnected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        components = n
        union = UnionFind(n)

        for i in range(n):
            for j in range(i + 1,n):
                if isConnected[i][j] and union.find(i) != union.find(j):
                    components -= 1
                    union.union(i,j)
        
        return components

