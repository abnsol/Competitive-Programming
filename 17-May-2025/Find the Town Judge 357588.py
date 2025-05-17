# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * n
        trusts = [0] * n
        for x,y in trust:
            trusted[y - 1] += 1
            trusts[x - 1] += 1

        for i in range(n):
            if trusted[i] == n - 1 and trusts[i] == 0:
                return i + 1
        
        return -1