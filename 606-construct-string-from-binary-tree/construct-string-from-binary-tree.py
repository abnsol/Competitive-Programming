# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            string = ""
            if not node:
                return string
            
            string += str(node.val)
            if not node.left and node.right:
                string += "()"
            elif not node.left and not node.right:
                return string

            if node.left:
                string += "(" + str(dfs(node.left)) + ")"
            if node.right:
                string += "(" + str(dfs(node.right)) + ")"
            
            return string
        
        return dfs(root)
            
