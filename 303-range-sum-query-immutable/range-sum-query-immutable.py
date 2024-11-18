class NumArray:

    def __init__(self, nums: List[int]):
        self.ps = [0]
        for i in range(len(nums)):
            self.ps.append(self.ps[i] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right + 1] - self.ps[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

'''
prefix sum
0 -2 -2 1 -4 -2 -3
n + 1 length ps arr
nums[right + 1] - nums[left]
'''  