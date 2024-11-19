class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        def decryption(code,k):
            ans = []
            for i in range(n):
                ttl = 0
                for j in range(1,k + 1):
                    idx = (i + j) % n
                    ttl += code[idx]
                ans.append(ttl)
            return ans
        
        if k > 0:
            return decryption(code,k)
        else:
            k *= -1
            print(list(reversed(code)))
            return decryption(code[::-1],k)[::-1]



'''
brute force
if k = 0 return [0] * n

def decrypt(code):
    ans = []
    for i in range(n):
        sum = 0
        for j in range(1,k + 1):
            idx = (i + j) % n
            sum += code[idx]
        ans.append(sum)
    return ans

if k > 0:
    return decrypt(code)
    
if k < 0:
    return decrypt(reversed(code)).reverse()         
'''
        