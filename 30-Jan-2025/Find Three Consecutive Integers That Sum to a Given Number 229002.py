# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        #find the one u can begin summing with 
        #ex : 33 doesnt need 0, 1, 2
        midVal = num // 3
        if midVal - 1 + midVal + midVal + 1 != num:
            return []
        else:
            return [midVal - 1,midVal, midVal + 1]

            




        