# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        for idx,num in enumerate(nums):
            if pos < idx:
                return False

            pos = max(idx + nums[idx],pos)  
        return True   