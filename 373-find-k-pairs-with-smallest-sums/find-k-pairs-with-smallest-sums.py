class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = [[u + nums2[0], i, 0] for i, u in enumerate(nums1[:k])]
        heapify(pq)

        res = []  

        while pq and k > 0:
            
            sum_pair, idx1, idx2 = heappop(pq)
          
            res.append([nums1[idx1], nums2[idx2]])
          
            k -= 1  

            if idx2 + 1 < len(nums2):
                heappush(pq, [nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1])

        return res
        