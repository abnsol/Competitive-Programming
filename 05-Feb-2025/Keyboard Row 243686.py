# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {}
        row = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        for i in range(3):
            for j in range(len(row[i])):
                dic[row[i][j]] = i
        
        ans = []
        for i in range(len(words)):
            flag = True
            row = dic[words[i][0].lower()]
            for j in words[i]:
                if dic[j.lower()] != row:
                    flag = False
                    break
            
            if flag:
                ans.append(words[i])
        
        return ans