# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = Counter(s)
        # print(cnt)
        seen = set()
        n = len(s)
        l = 0
        ans = []

        for r in range(n):
            seen.add(s[r])
            cnt[s[r]] -= 1
            if cnt[s[r]] == 0:
                seen.remove(s[r])
            
            if len(seen) == 0:
                ans.append(r - l + 1)
                l = r + 1
        
        return ans


        