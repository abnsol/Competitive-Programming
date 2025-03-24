# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        # if n == 1: return ["0","1"]
        ans = []
        def bt(sub):
            if len(sub) == n:
                ans.append("".join(map(str,sub)))
                return
            
            if sub[-1] != 0:
                sub.append(0)
                bt(sub[:])
                sub.pop()
            sub.append(1)
            bt(sub[:])

        bt([0])
        bt([1])
        return ans