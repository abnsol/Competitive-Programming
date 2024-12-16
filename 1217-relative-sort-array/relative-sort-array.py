class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maximum = max(arr1)
        cnt = [0] * (maximum + 1)
        for num in arr1:
            cnt[num] += 1
        
        ans = []
        for num in arr2:
            ans += [num] * cnt[num]
            cnt[num] = 0
    
        for value,remaining in enumerate(cnt):
            ans += [value] * remaining

        return ans

        