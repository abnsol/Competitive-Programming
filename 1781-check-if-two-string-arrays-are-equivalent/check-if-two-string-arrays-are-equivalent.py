class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        row1 = row2 = idx1 = idx2 = 0

        while row1 < len(word1) and row2 < len(word2):
            if word1[row1][idx1] != word2[row2][idx2]:
                return False
            idx1 += 1
            idx2 += 1
            
            if idx1 == len(word1[row1]):
                row1 += 1
                idx1 = 0
            
            if idx2 == len(word2[row2]):
                row2 += 1
                idx2 = 0

        return row1 == len(word1) and row2 == len(word2)
             
             