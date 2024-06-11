class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        arr = []

        for num in arr2:
            arr += ([num] * count[num])
            count[num] = 0
        
        count = sorted(count.items())
        for rem in count:
            arr += ([rem[0]] * rem[1])
        
        return arr

