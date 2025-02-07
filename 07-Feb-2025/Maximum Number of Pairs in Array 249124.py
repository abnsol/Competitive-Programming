# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = [0,0]
        for key in freq:
            ans[0] += freq[key] // 2
            ans[1] += freq[key] % 2

        return ans  
        