# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post(root,arr):
            if root == None:
                return arr
            
            left = post(root.left,arr)
            right = post(root.right,arr)
            return left + right + [root.val]
        
        arr = []
        return post(root,arr)