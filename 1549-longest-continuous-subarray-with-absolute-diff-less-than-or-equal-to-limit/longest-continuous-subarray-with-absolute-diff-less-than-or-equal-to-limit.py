class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque()
        min_q = deque()
        l = res = 0

        for r in range(len(nums)):
            while min_q and min_q[-1] > nums[r]:
                min_q.pop()
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()
            
            max_q.append(nums[r])
            min_q.append(nums[r])
            
            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[l]:
                    max_q.popleft()
                if min_q[0] == nums[l]:
                    min_q.popleft()
    
                l += 1
            
            res = max(res,r - l + 1)
        
        return res