class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        l = 0

        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                ans = max(ans,len(seen))
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
        
        return ans
            
            
