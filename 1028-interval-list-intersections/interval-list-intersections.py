class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m,n = len(firstList),len(secondList)
        s1 = s2 = i = j = 0
        e1 = e2 = 1
        ans = []

        while i < m and j < n:
            if firstList[i][s1] > secondList[j][e2]:
                j += 1
            elif firstList[i][e1] < secondList[j][s2]:
                i += 1
            else:
                interval = [max(firstList[i][s1],secondList[j][s2]),\
                            min(firstList[i][e1],secondList[j][e2])]
                ans.append(interval)
                if firstList[i][e1] > secondList[j][e2]:
                    j += 1
                else:
                    i += 1
            
        return ans




'''
                       l r
[[0,2],[5,10],[13,23],[24,25]]
                l r
[[1,5],[8,12],[15,24],[25,26]]

s1= 0
s2 = 0
e1 = 1
e2 = 1
firstList[i][s1] > secondList[j][e1]
    j += 1
firs < sec
    i += 1
max[s1] [s2] and min[e1][e2]

'''