# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_tree = []
        def inorder(root):
            if not root:
                return
            
            if root.left:inorder(root.left)
            sorted_tree.append(root.val)
            if root.right:inorder(root.right)
        
        def createBalanced(sorted_tree):
            if not sorted_tree:
                return None

            m = len(sorted_tree) // 2
            node = TreeNode(sorted_tree[m])
            node.left = createBalanced(sorted_tree[:m])
            node.right = createBalanced(sorted_tree[m + 1:])

            return node  

        inorder(root)
        return createBalanced(sorted_tree) 
    

        


        
        