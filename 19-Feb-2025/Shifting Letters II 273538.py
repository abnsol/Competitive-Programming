# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        rangeUpdate = [0] * (n + 1)

        for start,end,direction in shifts:
            if direction == 0:
                rangeUpdate[start] -= 1
                rangeUpdate[end + 1] += 1
            else:
                rangeUpdate[start] += 1
                rangeUpdate[end + 1] -= 1
        
        print(rangeUpdate)
        acc = 0
        ans = []
        for num in range(n):
            acc += rangeUpdate[num]
            print(acc)
            shifted = chr((ord(s[num]) + acc - 97) % 26 + 97)
            ans.append(shifted)
        
        return "".join(ans)




        print(ord("z"))
        print((96 - 97) % 26) 
        # 0 - 26
        # z => 122 - 97


        