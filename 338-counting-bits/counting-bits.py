class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        def counter(num):
            count = 0
            while num:
                num = num & (num - 1)
                count += 1
            
            return count
        
        for i in range(n + 1):
            ans.append(counter(i))
        
        return ans