class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ana = Counter(p)
        k = len(p)

        def isanam(window):
            count = Counter(window)
            for key in count.keys():
                if key in ana:
                    if ana[key] == count[key]:
                        continue
                    else:
                        return False
                else:
                    return False
            return True

        left = 0
        ans = []
        for right in range(k,len(s)+1):
            if isanam(s[left:right]):
                ans.append(left)
            left += 1

        return ans


