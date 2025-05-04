# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)

        def can_from_zero_array(query):
            diff_array = [0] * (n + 1)
            for i in range(query):
                st,en,val = queries[i]
                diff_array[st] += val
                diff_array[en + 1] -= val
            
            total = 0
            for i in range(n):
                total += diff_array[i]
                if total < nums[i]:
                    return False

            return True
        
        l, r = -1, len(queries) + 1
        while r > l + 1:
            m = (l + r) // 2
            if can_from_zero_array(m):
                r = m
            else:
                l = m
        
        return r if r <= q else -1






        
        