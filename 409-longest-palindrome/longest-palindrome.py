class Solution:
    def longestPalindrome(self, s: str) -> int:
        pal = Counter(s)
        oneCount = ans = 0

        for key in pal:
            if pal[key] % 2 == 0:
                ans += pal[key]
            else:
                if oneCount == 0:
                    ans += pal[key]
                    oneCount += 1
                else:
                    if pal[key] > 1:
                        ans += pal[key] - 1
        
        return ans
        