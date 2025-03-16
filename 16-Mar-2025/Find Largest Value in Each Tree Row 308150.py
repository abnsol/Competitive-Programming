# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        level_max = defaultdict(lambda:float("-inf"))
        def traverse(node,level):
            if not node:
                return 
            
            level_max[level] = max(level_max[level],node.val)
            if node.left: traverse(node.left,level + 1)
            if node.right: traverse(node.right, level + 1)
            return 

        traverse(root,0) 
        return list(level_max.values())