# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        range_update = [0] * 1001
        for num,fro,to in trips:
            range_update[fro] += num
            range_update[to] -= num
            # print(range_update)
        
        # print(range_update)
        presum = list(accumulate(range_update))
        # print(list(presum))
        return max(presum) <= capacity       