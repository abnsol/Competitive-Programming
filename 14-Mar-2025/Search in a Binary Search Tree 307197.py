# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val == val:
            return root

        if not root.left and not root.right:
            return None
        
        if root.val > val and root.left:
            return self.searchBST(root.left,val)
        elif root.val < val and root.right:
            return self.searchBST(root.right,val)
        else:
            return None

        