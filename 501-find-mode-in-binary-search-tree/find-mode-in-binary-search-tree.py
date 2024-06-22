# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def counter(root,count):
            if root == None:
                return count
            
            count[root.val] = count.get(root.val,0) + 1
            count = counter(root.left,count)
            count = counter(root.right,count)

            return count

        allnodes = counter(root,{})
        maxim = 0 
        ans = []
        for key in allnodes:
            if allnodes[key] > maxim:
                maxim = allnodes[key]
                ans = [key]
            elif allnodes[key] == maxim:
                ans.append(key)
        
        return ans

            
        