class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.rstrip()
        idx = -1
        count = 0
        while len(a) + idx >= 0 and a[idx] != " ":
            count += 1
            idx -= 1
        
        return count