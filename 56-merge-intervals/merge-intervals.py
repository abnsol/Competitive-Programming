class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        n = len(intervals)
        for i in range(1,n):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[i][1],ans[-1][1])
            else:
                ans.append(intervals[i])
        return ans

'''
returnArr = [[1,6],[8,10],[15,18]]

pseudocode

ans = [intervals[0]]
FOR i from 1 to n:
    IF intervals[i][0] <= ans[-1][1]:
        ans[-1][1] = intervals[i][1]
    Else:
        ans += intervals[i]
    ENDIF
ENDFOR
RETURN ans
'''