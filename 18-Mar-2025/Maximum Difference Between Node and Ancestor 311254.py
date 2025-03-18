# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root,min_val,max_val,cur_val):
            if not root: return cur_val
            res_min = abs(min_val - root.val)
            res_max = abs(max_val - root.val)
            cur_val = max(res_min,res_max,cur_val)
            min_val = min(min_val,root.val)
            max_val = max(max_val,root.val)  
            left = helper(root.left,min_val,max_val,cur_val)     
            right = helper(root.right,min_val,max_val,cur_val)

            return max(left,right,cur_val)

        return helper(root,root.val,root.val,0)






#lets keep track of the min and max val and 
#return the max of the difference of maxval - curval and min val - cur val
        