class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recurse(n):
            if n == 1:
                return '0'
            
            s = recurse(n-1)
            return str(s) + "1" + reverse(inverse(s))
            
        
        def reverse(string):
            return string[::-1]
        
        def inverse(bits):
            ans = ""
            for i in bits:
                if i == '0':
                    ans += '1'
                else:ans += '0'
            return ans
        
        ans = recurse(n)
        return ans[k - 1]


'''
base case 
when n = 1

recursive calls
call recursive, reverse fn, inverse fn

'''