# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.q = deque()
        self.k = k 
        self.cnt = 0
        self.value = value       

    def consec(self, num: int) -> bool:
        if len(self.q) == self.k:
            self.cnt -= 1 if self.q.popleft() == self.value else 0
        
        self.q.append(num)
        self.cnt += 1 if num == self.value else 0
        return self.cnt == self.k
        
        
        


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)