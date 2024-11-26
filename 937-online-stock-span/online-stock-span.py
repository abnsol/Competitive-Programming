class StockSpanner:

    def __init__(self):
        self.stk = []
        

    def next(self, price: int) -> int:
        new = [price,1]
        while self.stk and self.stk[-1][0] <= new[0]:
            price, span = self.stk.pop()
            new[1] += span

        self.stk.append(new)
        return new[1] 
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)