# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        add, sub = ["X++","++X"], ["X--","--X"]
        x = 0
        for op in operations:
            if op in add:
                x += 1
            else:
                x -= 1
        return x
                
            
        