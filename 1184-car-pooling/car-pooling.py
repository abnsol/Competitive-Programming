class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 1000
        rangeUpdate = [0] * (n + 1)

        for num,start,end in trips:
            rangeUpdate[start] += num
            rangeUpdate[end] -= num
        print(rangeUpdate)

        acc = 0
        for num in rangeUpdate:
            acc += num
            if acc > capacity:
                return False

        return True 
        