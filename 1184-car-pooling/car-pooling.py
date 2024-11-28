class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        rangeUpdate = [0] * (1001)

        for passanger,start,to in trips:
            rangeUpdate[start] += passanger
            rangeUpdate[to] -= passanger
        
        acc = 0
        for num in rangeUpdate:
            if acc > capacity:
                return False
            acc += num

        return True    