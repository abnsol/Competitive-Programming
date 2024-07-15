from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(start, target, path):
            if target == 0:
                ans.append(path[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                bt(i + 1, target - candidates[i], path)
                path.pop()
        
        ans = []
        candidates.sort()
        bt(0, target, [])
        return ans
