class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        numberOfOps = 0

        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                numberOfOps += 1
                l += 1
                r -= 1
        
        return numberOfOps


'''
Two pointers approach

sort
intialize pointers
create numberofoperation = 0
iterating while l < r
 check if sum != target(k)
    increase accly
 is
    increase the numberofoperations by one 
    chnge both pointers
return numberof operation
'''