class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        ans = []
        for num in arr2:
            ans += [num] * cnt[num]
            del cnt[num]
        
        left = []
        for keys in cnt:
            left += [keys] * cnt[keys]
        
        left.sort()
        ans += left

        return ans

        