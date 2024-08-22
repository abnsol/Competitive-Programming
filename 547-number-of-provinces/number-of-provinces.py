class Union:
    def __init__(self,size):
        self.parent = {i:i for i in range(size)}
        self.rank = [0] * size

    def find(self,x):
        if x == self.parent[x]:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
            elif self.rank[parentX] < self.parent[parentY]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentX] = parentY
                self.rank[parentY] += 1
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        union = Union(size)
        numberOfComponents = size

        for i in range(len(isConnected)):
            for j in range(i,size):
                if isConnected[i][j] and union.find(i) != union.find(j):
                    union.union(i,j)
                    numberOfComponents -= 1
        
        return numberOfComponents