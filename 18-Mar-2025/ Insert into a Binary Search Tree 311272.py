# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root: return node
        
        if val < root.val:
            if root.left:self.insertIntoBST(root.left,val)
            else: root.left = node
        elif val > root.val:
            if root.right: self.insertIntoBST(root.right,val)
            else: root.right = node
        
        return root

    # def insertVal(self,root,val):
        

        
        