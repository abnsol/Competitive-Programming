class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = j = 0
        w1 = len(word1)
        w2 = len(word2)
        merge = []
        while i < w1 and j < w2:
            if word1[i:] < word2[j:]:
                merge.append(word2[j])
                j += 1
            else:
                merge.append(word1[i])
                i += 1
        
        merge += word1[i:]
        merge += word2[j:]
        return "".join(merge)
            