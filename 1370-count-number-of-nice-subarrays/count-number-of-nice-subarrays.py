class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = l = count = total = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                count += 1
                total = 0
            
            while count == k:
                total += 1
                if nums[l] % 2 == 1:
                    count -= 1
                l += 1
            print(total)
            ans += total
            
        return ans