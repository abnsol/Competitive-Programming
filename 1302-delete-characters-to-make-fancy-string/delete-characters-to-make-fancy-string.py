class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        prev = answer = s[0]
        prevCharCount = 1

        for i in range(1,n):
            if s[i] == prev and prevCharCount >= 2:
                continue
            
            answer += s[i]
            if s[i] == prev:
                prevCharCount += 1
            else:
                prev = s[i]
                prevCharCount = 1
        
        return answer
        
        
        
'''
prev distint char = s[0]
number of the prev distinct char = 1
answer = s[0]

for i in s[1,n]:
    if i == prev and number of prev char > 2:
        continue
    
    answer += i
    if i == prev dis :
        num += 1
    else:
        prev dis = i
        numb = 1

O[N]
O[N]       
    
'''