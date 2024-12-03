class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        myMap = {}
        for i in range(n):
            myMap[i] = -1 
        
        stk = []
        for i in range(2*n):
            i %= n
            while stk and stk[-1][1] < nums[i]:
                index,popped_num = stk.pop()
                myMap[index] = nums[i]

            if myMap[i] == -1:
                stk.append([i,nums[i]])
        
        ans = [0] * n
        for keys in myMap:
            ans[keys] = myMap[keys]
        
        return ans        

'''
1 : 2
1 : 2
[2,2]

'''