class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, path_sum):
            if not node:
                return 0
            path_sum = path_sum * 10 + node.val
            if not node.left and not node.right:
                return path_sum
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)
        
        return dfs(root, 0) 