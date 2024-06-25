class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        maps = {'2' : ['a','b','c'],
                '3' : ['d','e','f'],
                '4' : ['g','h','i'],
                '5' : ['j','k','l'],
                '6' : ['m','n','o'],
                '7' : ['p','q','r','s'],
                '8' : ['t','u','v',],
                '9' : ['w','x','y','z']}
        

        def bt(idx,string):
            if idx >= len(digits):
                res.append(''.join(string))
                return
            
            mapping = maps[digits[idx]]
            for i in range(len(mapping)):
                string.append(mapping[i])
                bt(idx + 1,string)
                string.pop()
        
        res = []
        for i in maps[digits[0]]:
            bt(1,[i])
        return res




'''
maps = {2: abc
        3: def
        4: ghi
        5: jkl
        6: mno
        7: pqrs
        8: tuv
        9: wxyz }
'''