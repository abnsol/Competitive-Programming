class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)  
        need = {}  
        for num in nums:
            if freq[num] == 0:
                continue
            elif need.get(num, 0) > 0:
                need[num] -= 1
                need[num + 1] = need.get(num + 1, 0) + 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] = need.get(num + 3, 0) + 1
            else:
                return False
            freq[num] -= 1 
        
        return True