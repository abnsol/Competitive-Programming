# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet:
    def __init__(self):
        self.num_idx = {}
        self.nums = []
        self.idx = 0
        
    def insert(self, val: int) -> bool:
        if val not in self.num_idx:
            self.nums.append(val)
            self.num_idx[val] = self.idx
            self.idx += 1
            # print("nums",self.nums)
            # print("dic",self.num_idx)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.num_idx:
            val_idx = self.num_idx[val]
            self.num_idx[self.nums[self.idx - 1]] = val_idx
            self.nums[val_idx],self.nums[self.idx - 1] = \
            self.nums[self.idx - 1],self.nums[val_idx]
            self.nums.pop()
            del self.num_idx[val]
            self.idx -= 1
            return True
        return False

    def getRandom(self) -> int:
        rand = random.randrange(0,len(self.nums))
        return self.nums[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()