# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ttl = 0
        def dfs(node,prev):
            val = prev * 10 + node.val
            if not node.right and not node.left:
                self.ttl += val
                return
            
            if node.left:
                dfs(node.left,val)
            if not node.left or node.right:
                dfs(node.right,val)
            
            
            
        dfs(root,0)
        return self.ttl
        
            
