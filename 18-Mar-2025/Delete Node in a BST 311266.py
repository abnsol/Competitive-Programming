# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        # search phase
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            # handles if no or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left # predecessor
            
            # find the successor
            cur = root.right
            while cur.left:
                cur = cur.left
            
            root.val = cur.val 
            # delete the replaced
            root.right = self.deleteNode(root.right,root.val) 
        
        return root