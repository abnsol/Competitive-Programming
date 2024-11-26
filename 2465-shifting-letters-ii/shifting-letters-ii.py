class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        rangeUpdate = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                rangeUpdate[start] += 1
                rangeUpdate[end + 1] -= 1
            else:
                rangeUpdate[start] += -1
                rangeUpdate[end + 1] -= -1
        
        acc = 0
        ans = ''
        for i in range(n):
            acc += rangeUpdate[i]
            shifted_letter = (ord(s[i]) - 97 + acc) % 26 + 97
            ans += chr(shifted_letter)
        
        return ans