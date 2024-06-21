# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
        def sym(r1,r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False

            return (r1.val == r2.val and sym(r1.left,r2.right) and sym(r1.right,r2.left))

        return sym(root.left,root.right) 
        

