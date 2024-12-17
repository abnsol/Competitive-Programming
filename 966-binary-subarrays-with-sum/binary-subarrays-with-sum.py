class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ps = {0 : 1}
        ttl = 0
        res = 0

        for num in nums:
            ttl += num
            if ttl - goal in ps:
                res += ps[ttl - goal]
            ps[ttl] = ps.get(ttl,0) + 1 
        
        return res
        
'''
x - ps = goal
x - goal = ps
'''