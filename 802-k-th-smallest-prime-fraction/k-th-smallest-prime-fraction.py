class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        div = []

        for i in range(len(arr)):
            for j in range(i,len(arr)):
                div.append([arr[i]/arr[j],[arr[i],arr[j]]])
        
        div.sort()
        return div[k - 1][1]