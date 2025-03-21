# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ttl = [0]

        def inorder(root):
            if not root:
                return 0
            
            inorder(root.right)
            temp = root.val
            root.val += ttl[0]
            ttl[0] += temp
            inorder(root.left)
        
        inorder(root)
        return root


