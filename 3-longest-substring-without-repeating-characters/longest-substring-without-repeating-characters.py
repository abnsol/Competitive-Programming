class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = {}
        l = 0
        res = 0

        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r],0) + 1
            while cnt[s[r]] > 1:
                cnt[s[l]] -= 1
                l += 1
            
            res = max(res,r - l + 1)
        
        return res
        



'''
sliding window approach

cnt = elem => occurence

add(x) : => cnt[x] += 1
removing(x): => cnt[x] -= 1
good(): cnt[x] <= 1 
'''
        