# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = []
        n = len(nums) // 3
        for key in cnt:
            if cnt[key] > n:
                ans.append(key)
        
        return ans
