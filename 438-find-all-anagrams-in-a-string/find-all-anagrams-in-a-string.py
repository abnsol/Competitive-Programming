class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        k = len(p)

        if len(s) < k:
            return []

        pCount = Counter(p)

        windowCount = {}
        for i in range(k):
            windowCount[s[i]] = windowCount.get(s[i],0) + 1
        
        if pCount == windowCount:
            ans.append(0)
        
        for _ in range(k,len(s)):
            if windowCount[s[_ - k]] == 1:
                del windowCount[s[_ - k]]
            else:
                windowCount[s[_ - k]] -= 1
            
            windowCount[s[_]] = windowCount.get(s[_],0) + 1
            if pCount == windowCount:
                ans.append(_ - k + 1)

        return ans

        


'''
fixed sliding window approach
ans = []
p = Counter(p)


p = {a : 1, b : 1 , c : 1}
k = len(p)

secondMap = {}
for i in range(k):
    add s[i] in secondMap

if SecondMap == p:
    add 0 to ans

for _ in range(k,len(s)):
    if SecondMap[s[k]] == 1:
        remove SecondMap[s[k]] from map
    else:
        SecondMap[s[k]] -= 1
    SecondMap.add(s[_])
    if SecondMap == p:
        add _ + k to ans

return ans
'''