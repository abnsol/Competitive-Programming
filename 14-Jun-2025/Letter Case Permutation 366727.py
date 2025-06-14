# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution(object):
    def letterCasePermutation(self, S):
        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub + S[i], i + 1)
                
        res = []
        backtrack()
        return res