class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = max(citations)
        cnt_srt = [0] * (n + 1)

        for cite in citations:
            cnt_srt[cite] += 1
        
        numbersAfter = 0
        for i in range(n,-1,-1):
            numbersAfter += cnt_srt[i]
            if numbersAfter >= i:
                return i
        
        return 0


'''
count_srt solution  
'''