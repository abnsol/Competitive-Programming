class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # range query update
        n = len(s)
        # difference array(diff) to register the shifts
        # which only affects the first and last elements of the range
        diff = [0] * (n + 1) # n + 1 to handle if the shift occurs on last element
        
        # iterate through shifts and register shifts
        for start,end,direction in shifts:
            if direction == 0:
                diff[start] -= 1
                diff[end + 1] += 1
            else:
                diff[start] += 1
                diff[end + 1] -= 1
        
        for i in range(1,n + 1): diff[i] += diff[i - 1]
        
        ans = []
        #ans = [chr(ord('a') + (ord(s[i] - ord('a') + diff[i] + 26) % 26)) for i in range(n)] 
        for i in range(n):
            temp = chr(ord('a') + (ord(s[i]) - ord('a') + diff[i] + 26) % 26)
            ans.append(temp)
        
        return "".join(ans)