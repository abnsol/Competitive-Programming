# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root, 1)])
        
        while q:
            cur = q[-1][1] - q[0][1] + 1
            ans = max(ans, cur)
            
            for _ in range(len(q)):
                node, index = q.popleft()
                
                if node.left:
                    q.append((node.left, 2 * index))
                    
                if node.right:
                    q.append((node.right, 2 * index + 1))
        
        return ans








            
