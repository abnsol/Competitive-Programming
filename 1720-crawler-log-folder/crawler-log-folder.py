class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for char in logs:
            if stk and char == "../":
                stk.pop()
            elif char != '../' and char != "./":
                stk.append(char)
        
        return len(stk)
        