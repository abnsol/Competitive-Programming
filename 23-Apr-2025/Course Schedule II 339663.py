# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for x,y in prerequisites:
            g[y].append(x)
            indegree[x] += 1
        
        q = deque([i for i in range(numCourses) if not indegree[i]])
        order = []
        while q:
            vertex = q.popleft()
            order.append(vertex)
            for child in g[vertex]:
                indegree[child] -= 1
                if not indegree[child]: 
                    q.append(child)
            
        if len(order) != numCourses:
            return []
        
        return order
        



        