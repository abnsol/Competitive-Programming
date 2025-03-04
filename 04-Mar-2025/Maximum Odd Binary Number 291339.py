# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s)
        ans = ["1"] * (cnt["1"] - 1) + ["0"] * (cnt["0"]) + ["1"]
        return "".join(ans)
        
        