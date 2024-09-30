class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")

        filterWords = []
        for word in words:
            x,y = word[:-1],int(word[-1])
            filterWords.append([x,y])
        
        filterWords.sort(key = lambda x : x[1])
        
        ans = ''
        for word,idx in filterWords:
            ans += (word + " ")
            
        return ans.rstrip()


        