class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.cnt = 0
        self.intstream = deque()


    def consec(self, num: int) -> bool:
        self.intstream.append(num)
        if num == self.value:
            self.cnt += 1
            
        if len(self.intstream) < self.k: return False
        else:
            if self.cnt == self.k:
                self.cnt -= 1
                self.intstream.popleft()
                return True
            
            if self.intstream[0] == self.value: self.cnt -= 1 
            self.intstream.popleft()
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)