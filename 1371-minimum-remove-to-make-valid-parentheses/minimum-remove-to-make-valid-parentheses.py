class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for idx, c in enumerate(s):
            if c not in "()":
                continue

            if stack and stack[-1][1] + c == "()":
                stack.pop()
            else:
                stack.append((idx,c))

        res = [] 
        for idx, c in enumerate(s):
            if (idx,c) not in stack:
                res.append(c)

        return "".join(res)
