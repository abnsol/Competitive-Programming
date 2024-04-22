class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = Counter()
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                n = stack.pop()
                greater[n] = num
            stack.append(num)
        
        n = len(nums1)
        res = [greater[nums1[i]] if nums1[i] in greater else -1 for i in range(n)]
       
        return res

