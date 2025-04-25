# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [0] * numCourses
        g = defaultdict(list)
        for x,y in prerequisites:
            g[x].append(y)
        
        def dfs(node):
            if color[node] == 2:return True

            res = True
            color[node] = 1 #gray

            for child in g[node]:
                if color[child] == 1:
                    return False

                res = res and dfs(child)

            color[node] = 2
            return res
        
        ans = True
        for i in range(numCourses):
            if color[i] == 0:
                ans = ans and dfs(i)    

        return ans  