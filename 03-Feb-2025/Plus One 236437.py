# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(map(str,digits)))
        integer += 1
        ans = []
        while integer > 0:
            ans.append(integer % 10)
            integer //= 10
        
        return list(reversed(ans))
        