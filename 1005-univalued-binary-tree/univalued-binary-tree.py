# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = set()
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                val.add(node.val)
                q.append(node.left)
                q.append(node.right)
        
        return len(val) == 1