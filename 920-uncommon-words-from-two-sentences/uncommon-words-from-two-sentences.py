class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        countString1 = Counter(s1.split(" "))
        countString2 = Counter(s2.split(" "))

        ans = []

        for key in countString1:
            if key not in countString2 and countString1[key] <= 1:
                ans.append(key)
        
        for key in countString2:
            if key not in countString1 and countString2[key] <= 1:
                ans.append(key)
        
        return ans