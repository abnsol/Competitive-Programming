# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = []
        n = len(nums) // 3
        for key in cnt:
            if cnt[key] > n:
                ans.append(key)
        
        return ans
