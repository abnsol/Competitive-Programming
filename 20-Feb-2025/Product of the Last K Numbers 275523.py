# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.prod = 1
        self.last_zero = float("-inf")
        self.prefix_prods = []
        
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prods.append(0)
            self.prod = 1
            self.last_zero = len(self.prefix_prods) - 1
        else:
            self.prod *= num
            self.prefix_prods.append(self.prod)        

    def getProduct(self, k: int) -> int:
        idx = len(self.prefix_prods) - k - 1
        if idx < self.last_zero: return 0
        if idx == self.last_zero: 
            return self.prefix_prods[-1] 
        elif idx != float("-inf") and idx < 0:
            return self.prefix_prods[-1]
        else:
            return self.prefix_prods[-1]//self.prefix_prods[idx]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)