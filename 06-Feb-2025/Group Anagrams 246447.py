# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word = defaultdict(list)
        for word in strs:
            sWord = "".join(sorted(word))
            sorted_word[sWord].append(word)
        
        return list(sorted_word.values())
                