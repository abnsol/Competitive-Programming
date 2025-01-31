# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a ,b = "Fizz" ,"Buzz"
        ans = []
        for i in range(1,n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append(a + b)
            elif i % 5 == 0:
                ans.append(b)
            elif i % 3 == 0:
                ans.append(a)
            else:
                ans.append(str(i))
        
        return ans

        