# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def inorder(root,arr):
            if root == None:
                return arr
            
            left = inorder(root.left,arr)
            right = inorder(root.right,arr)

            return left + [root.val] + right
        
        return inorder(root,arr)