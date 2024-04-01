class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        count = [0] * len(words)

        for word in words:
            count[int(word[-1]) - 1] = word[:len(word) - 1]
        
        return " ".join(count)