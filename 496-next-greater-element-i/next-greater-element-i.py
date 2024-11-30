class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        nextGreater = {}

        for num in nums2:
            while stk and stk[-1] < num:
                popped = stk.pop()
                nextGreater[popped] = num
            
            stk.append(num)
        
        ans = []
        for num in nums1:
            if num in nextGreater:
                ans.append(nextGreater[num])
            else:
                ans.append(-1)
        
        return ans

        