# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def bt(st,combination):
            if st > n + 1:
                return 

            if len(combination) == k:
                ans.append(combination[:])
                return
            
            combination.append(st)
            bt(st + 1,combination)
            combination.pop()
            bt(st + 1,combination)

        
        bt(1,[])
        return ans
