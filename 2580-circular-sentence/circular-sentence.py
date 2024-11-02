class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # sentence = sentence.strip()
        # print(sentence)
        splitSentence = sentence.split()
        n = len(splitSentence)

        if n == 1 :
            return sentence[0] == sentence[-1]
                
        for i in range(1,n):
            if splitSentence[i][0] != splitSentence[i - 1][-1]:
                return False
            
            if i == n - 1:
                if splitSentence[i][-1] != splitSentence[0][0]:
                    return False

        return True

