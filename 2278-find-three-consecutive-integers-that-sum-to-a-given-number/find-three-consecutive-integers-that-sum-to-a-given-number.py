class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        #find the one u can begin summing with 
        #ex : 33 doesnt need 0, 1, 2
        midVal = num // 3
        if midVal - 1 + midVal + midVal + 1 != num:
            return []
        else:
            return [midVal - 1,midVal, midVal + 1]

            




        