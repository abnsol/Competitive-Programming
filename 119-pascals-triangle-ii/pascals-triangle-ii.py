class Solution:
    def getRow(self, r: int) -> List[int]:
        if r == 0:
            return [1]     # first row
        arr = self.getRow(r - 1) # divide till first row
        res = [1] # all start with one 
        for i in range(len(arr) - 1): 
            res.append(arr[i] + arr[i + 1])# add consecutive elements in prev row
        res.append(1) # all end with 1
        return res