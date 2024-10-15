class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        counter = {}
        l = 0 
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r],0) + 1
            while counter[s[r]] > 1 and l < r:
                counter[s[l]] -= 1
                l += 1
            
            longest = max(longest,r - l + 1)
        
        return longest
            
