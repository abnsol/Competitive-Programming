# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        scnt = Counter(s)
        tcnt = Counter(t)

        for key in tcnt:
            if key not in scnt or scnt[key] < tcnt[key]:
                return key
        