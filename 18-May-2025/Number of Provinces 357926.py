# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UF(n)
        for i in range(n):
            for j in range(i + 1):
                if isConnected[i][j] == 1:
                    dsu.unionSet(i,j)
        
        return dsu.numberOfSets()




class UF:
    def __init__(self,size):
        self.pSet = {i:i for i in range(size)} # parent set
        self.setSize = {i:1 for i in range(size)} # size of current set
        self.numSets = size # number of disjoint sets
    
    def findSet(self,item):
        if self.pSet[item] == item: return item # parent same as item 

        # path comprehension
        self.pSet[item] = self.findSet(self.pSet[item]) # parent of item will be directly assigned to 1 parent
        return self.pSet[item]

    def unionSet(self,item1,item2):
        parent1 = self.findSet(item1)
        parent2 = self.findSet(item2)
        if parent1 != parent2:
            self.setSize[parent2] += 1
            self.numSets -= 1
            self.pSet[parent1] = parent2

        return self.pSet[item1]

    def connected(self,item1,item2):
        return self.findSet(item1) == self.findSet(item2) 
    
    def sizeOfSet(self,item):
        return self.setSize[self.findSet(item)]
            
    def numberOfSets(self):
        return self.numSets
            


'''
[1,1,0]
[1,1,0]
[0,0,1]
'''

