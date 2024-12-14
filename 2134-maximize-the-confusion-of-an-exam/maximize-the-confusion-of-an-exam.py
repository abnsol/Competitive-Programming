class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        def maxConsecutive(x):
            cnt = 0
            l = 0
            res = 0

            for r in range(n):
                if answerKey[r] == x:
                    cnt += 1
                
                while cnt > k:
                    if answerKey[l] == x:
                        cnt -= 1
                    l += 1

                res = max(res,r - l + 1)

            return res

        return max(maxConsecutive("F"),maxConsecutive("T")) 
                    

        