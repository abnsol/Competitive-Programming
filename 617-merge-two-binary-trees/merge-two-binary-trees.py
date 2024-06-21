# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def insert(root1,root2):
            root = TreeNode()
            if not root1 and not root2:
                return 
            
            if root1 == None and root2 != None:
                root = root2
            elif root1 != None and root2 == None:
                root = root1
            else:
                root.val = root1.val + root2.val
                root.left = insert(root1.left,root2.left)
                root.right = insert(root1.right,root2.right)
            
            
            return root
        
        return insert(root1,root2)
            

'''
call the left tree
call the right tree
if left.val = null
if right.val = null
both are null
'''