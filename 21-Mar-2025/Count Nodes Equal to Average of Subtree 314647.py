# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = [0]
        def dfs(root):
            if not root:
                return [0,0]
            
            l,a = dfs(root.left)
            r,b = dfs(root.right)

            ttl = l + r + root.val
            cnt = a + b + 1
            roo = ttl//cnt
            
            if root.val == ttl//cnt: ans[0] += 1  
            return [ttl,cnt]
        
        dfs(root)
        return ans[0]
        