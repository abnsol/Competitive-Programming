class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = max(citations)
        cnt_srt = [0] * (n + 1)

        for cite in citations:
            cnt_srt[cite] += 1
        
        before = 0
        print(cnt_srt)
        for i in range(n,-1,-1):
            before += cnt_srt[i]
            if before >= i:
                return i
        
        return 0


'''
ans = 0
[0,1,3,5,6] 
counter = {} # [number of ints,index] [>= i] [n - index >= i]

if nums[i] > n or 0: not an answer
if i = 1 
while nums[i] < i and i < n:
    i += 1


i = 5
while i >= 0:
    
'''