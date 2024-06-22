# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        def bfs(root,count):
            res = []
            q = deque()
            q.append(root)

            while q:
                qlen = len(q)
                level = []
                for i in range(qlen):
                    node = q.popleft()
                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)

                if level:
                    if count % 2 == 0:
                        res.append(level)
                    else:
                        res.append(level[::-1])
                    count += 1
            
            return res
        
        return bfs(root,0)
        

'''
count odd and even
'''
        