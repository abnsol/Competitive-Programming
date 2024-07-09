"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        maps = {}
        for i in range(len(employees)):
            maps[employees[i].id] = i
        
        def dfs(i,count):
            node = employees[maps[i]]
            count += node.importance
            if not node.subordinates:
                return count
            
            for ids in node.subordinates:
                count += dfs(ids,0)
            
            return count
        
        return dfs(id,0)