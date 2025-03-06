# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for cd in logs:
            if stk and cd == "../":
                stk.pop()
            elif cd != "../" and cd != "./":
                stk.append(cd)
        
        return len(stk)
