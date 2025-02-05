# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def anagram(self,check,word):
        cnt = Counter(word)
        word_cnt = Counter(check)
        for key in word_cnt:
            if word_cnt[key] > cnt[key]:
                return False
        return True


    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for word in words:
            if self.anagram(word,cnt):
                ans += len(word)
        
        return ans

        