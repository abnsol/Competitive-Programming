# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda t : t[0])
        res,minheap = [],[]
        i,time = 0,tasks[0][0]

        while minheap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minheap,[tasks[i][1],tasks[i][2]])
                i += 1
            
            if not minheap:
                time = tasks[i][0]
            else:
                proc,idx = heapq.heappop(minheap)
                time += proc
                res.append(idx)
            
        return res
        
