"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        self._max = 0
        def dfs(node,count):
            if not node.children:
                self._max = max(self._max,count)
                return 
            
            count += 1
            for nodes in node.children:
                dfs(nodes,count)
            count -= 1
        
        dfs(root,1)
        return self._max
