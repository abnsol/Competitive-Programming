# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        def dfs(gparent,parent):
            if not parent:
                return
            
            if gparent.val % 2 == 0:
                if parent.left:
                    self.total += parent.left.val
                if parent.right:
                    self.total += parent.right.val

            dfs(parent,parent.left)
            dfs(parent,parent.right)
        
        
        dfs(root,root.left)
        dfs(root,root.right)
        return self.total


        