# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)

        #find all the products 
        # count product frequency
        for i in range(n):
            for j in range(i + 1,n):
                mul = nums[i] * nums[j]
                freq[mul] = freq.get(mul,0) + 1
        
        #freq > 1
        #sum of n - 1 multiplied by 8 gives the answer 
        ans = 0
        for val in freq.values():
            if val > 1:
                ttl = sum(range(1,val))
                ans += (ttl * 8)
        
        return ans

                
                