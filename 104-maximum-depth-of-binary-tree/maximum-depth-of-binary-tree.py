# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def counter(root,count):
            if root == None:
                return count
            
            left = counter(root.left,count + 1)
            right = counter(root.right,count + 1)

            return max(left,right)
        
        return counter(root,0)

        