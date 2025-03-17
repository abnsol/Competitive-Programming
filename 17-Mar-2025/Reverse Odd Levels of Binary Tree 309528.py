# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(left,right,level):
            if not left:
                return 

            if level % 2 == 0:
                temp = left.val
                left.val = right.val
                right.val = temp

            helper(left.left,right.right,level + 1)
            helper(left.right,right.left,level + 1)

        helper(root.left,root.right,0)
        return root    