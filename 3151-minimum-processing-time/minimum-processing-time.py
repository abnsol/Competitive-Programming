class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()

        minTime = float('-inf')
        i = 0
        j = 4

        for time in processorTime:
            currMax = max(tasks[i:j]) + time
            i += 4
            j += 4
            minTime = max(currMax,minTime)
        
        return minTime