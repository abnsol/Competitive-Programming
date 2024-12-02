class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        l = 0

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()                
            
            if r >= k - 1:
                ans.append(nums[q[0]])
                l += 1
        
        return ans

            

'''
if q.len > k pop.left
while nums[r] > q[-1] pop.right
if right >= k - 1:
    ans.append(q[0])
[3,-1,-3]
'''