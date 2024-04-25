class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stks = []
        stkt = []


        for c in s:
            if c == '#':
                if stks:
                    stks.pop()
            else:
                stks.append(c)
            
        for d in t:
            if d == '#':
                if stkt:
                    stkt.pop()
            else:
                stkt.append(d)

        return stks == stkt
        