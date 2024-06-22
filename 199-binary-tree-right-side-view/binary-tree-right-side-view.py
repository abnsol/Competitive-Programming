# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def bfs(root):
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
                    res.append(level[-1])
            
            return res
        
        return bfs(root)
                



'''
queue = 1
stack = [] 
does 1 have a right child? 
yes
go to right covering 2 but what if 3 doesnt have a child
goes back to 2 then its right and left child 
where should we store it

'''