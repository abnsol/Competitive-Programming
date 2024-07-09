# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])

        while q:
            n = len(q)
            ttl = 0
            cnt = 0
            for i in range(n):
                node = q.popleft()
                if node:
                    ttl += node.val
                    cnt += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if cnt:
                ans.append(ttl/cnt)
        
        return ans