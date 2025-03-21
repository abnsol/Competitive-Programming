# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def dfs(nums):
            if not nums:
                return None

            mid = len(nums)//2 
            node = TreeNode(nums[mid])
            node.left = dfs(nums[:mid])
            node.right = dfs(nums[mid+1:])
            
            return node
        return dfs(nums)
