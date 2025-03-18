# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, prevSum):
            if not root.left and not root.right:
                return prevSum + root.val

            prevSum = 10 * (prevSum + root.val)
            left = right = 0

            if root.left: left = helper(root.left, prevSum)
            if root.right: right = helper(root.right, prevSum)

            return left + right
           
        
        return helper(root, 0)