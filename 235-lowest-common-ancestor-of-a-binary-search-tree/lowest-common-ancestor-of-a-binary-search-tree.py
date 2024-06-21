# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        maxim = max(p.val,q.val)
        minim = min(p.val,q.val)

        if minim == root.val or maxim == root.val:
            return root

        if minim < root.val and maxim > root.val:
            return root
        elif minim > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return self.lowestCommonAncestor(root.left,p,q)



'''
bst
maxi = max(p,q)
mini = mini(p,q)
if mini < root.val and maxi > root.val:
    return root

if maxi > root.val:
    search in the root.right
else:
    search in the root.left

if u get 1 of the numbers return it

'''