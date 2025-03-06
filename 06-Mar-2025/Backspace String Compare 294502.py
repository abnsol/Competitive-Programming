# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stks = []
        stkt = []
        for i in s:
            if stks and i == '#':
                stks.pop()
            elif i != '#':
                stks.append(i)
        
        for i in t:
            if stkt and i == '#':
                stkt.pop()
            elif i != '#':
                stkt.append(i)
        
        return stks == stkt

