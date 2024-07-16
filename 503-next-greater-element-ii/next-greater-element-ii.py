class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1]*len(nums)
        stack = []
        stack.append([nums[0],0])
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][0]:
                result[stack[-1][1]] = nums[i]
                stack.pop()
            stack.append([nums[i],i])
        i=0
        index_val=stack[0][1]
        while(i<=index_val):
            while stack and nums[i] > stack[-1][0]:
                result[stack[-1][1]] = nums[i]
                stack.pop()
            i+=1
        return result

        return result