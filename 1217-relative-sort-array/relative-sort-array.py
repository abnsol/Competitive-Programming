class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idx1 = 0
        for num in arr2:
            idx2 = idx1
            while num in arr1[idx2:] and idx2 < len(arr1):
                if arr1[idx2] == num:
                    arr1[idx1], arr1[idx2] = arr1[idx2], arr1[idx1]
                    idx1 += 1
                idx2 += 1

        for i in range(idx2,len(arr1)):
            for j in range(idx2 + 1,len(arr1)):
                if arr1[j] < arr1[j - 1]:
                    arr1[j - 1], arr1[j] = arr1[j], arr1[j - 1] 

        return arr1
