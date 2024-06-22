# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root,minim,maxim):
            if not root:
                return maxim - minim
            
            maxim = max(maxim,root.val)
            minim = min(minim,root.val)

            left = dfs(root.left,minim,maxim)
            right = dfs(root.right,minim,maxim)

            return max(left,right)
        
        return dfs(root,root.val,root.val)
            
        