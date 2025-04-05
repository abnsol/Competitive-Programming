# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        indexes = [row.count(1) for row in mat]
        max_count = max(indexes)
        
        for i in range(len(mat)):
            if indexes[i]==max_count:
                return [i, indexes[i]]