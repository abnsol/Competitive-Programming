class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        count = [0] * len(words)

        for word in words:
            idx = int(word[-1])
            count[idx - 1] = word[:len(word) - 1]
        
        return " ".join(count)