class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        rowOne = rowTwo = 0
        ans = []

        while rowOne < len(firstList) and rowTwo < len(secondList):
            startOne , endOne = firstList[rowOne]
            startTwo , endTwo = secondList[rowTwo]

            startRange = max(startOne,startTwo)
            endRange = min(endOne,endTwo)

            if startRange <= endRange:
                ans.append([startRange,endRange])
            
            if endOne < endTwo:
                rowOne += 1
            else:
                rowTwo += 1

        return ans


        