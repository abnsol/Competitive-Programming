class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        freq = Counter(s)
        unique = set()

        for letter in s:
            if letter in unique:
                freq[letter] -= 1
                continue

            while stk and stk[-1] >= letter and freq[stk[-1]] > 1:
                popped = stk.pop()
                unique.remove(popped)
                freq[popped] -= 1
            
            stk.append(letter)
            unique.add(letter)
        
        return "".join(stk)

'''
bcabc
b : 2
c : 2
a : 1
[a,c,b]
"cbacdcbc"
c : 4
b : 2
a : 1
d : 1
do we have the other greater element
is the element entering already in the set
[a,c,d,b]
'''