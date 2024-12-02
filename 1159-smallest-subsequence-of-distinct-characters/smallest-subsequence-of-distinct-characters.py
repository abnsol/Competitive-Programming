class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stk = []
        unique = set()
        freq = Counter(s)

        for letter in s:
            if letter in unique:
                freq[letter] -= 1
                continue
            
            while stk and stk[-1] > letter and freq[stk[-1]] > 1:
                popped = stk.pop()
                freq[popped] -= 1
                unique.remove(popped)

            stk.append(letter)
            unique.add(letter)

        return "".join(stk)

        