class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if not stack:
                stack.append([c,1])
                continue

            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
                    
            else:
                stack.append([c,1])
        
        ans = ""
        for c,val in stack:
            ans += c*val
        
        return ans

