class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num,count in counter.items():
            bucket[count] += [num] 

        ans = []
        for i in range(len(nums),-1,-1):
            if k != len(ans):
                if bucket[i] != []:
                    ans += bucket[i]
            else:
                return ans
            
        return ans


