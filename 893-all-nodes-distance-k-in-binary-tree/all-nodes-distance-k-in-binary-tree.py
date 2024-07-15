# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)

        def createGraph(child,parent):
            if child and parent:
                g[parent.val].append(child.val)
                g[child.val].append(parent.val)
            
            if child.left:
                createGraph(child.left,child)
            if child.right:
                createGraph(child.right,child)
        
        createGraph(root,None)
        ans = []
        q = deque([(target.val,0)])
        visited = {target.val}

        while q:
            val,distance = q.popleft()
            
            if distance == k:
                ans.append(val)
                continue
            

            for neighbor in g[val]:
                if neighbor not in visited:
                    q.append((neighbor,distance + 1))
                    visited.add(neighbor)
        
        return ans