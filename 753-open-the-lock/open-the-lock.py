class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def helper(lock):
            children = []
            for i in range(len(lock)):
                digit = str((int(lock[i]) + 1) % 10)
                children.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) + 9) % 10)
                children.append(lock[:i] + digit + lock[i + 1:])
            
            return children

        q = deque([('0000',0)]) #locks and turns
        visited = set(deadends)
        while q:
            locks,turns = q.popleft()
            if locks == target:
                return turns
            
            for child in helper(locks):
                if child not in visited:
                    visited.add(child)
                    q.append((child,turns + 1))
        
        return -1