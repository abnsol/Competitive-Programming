class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def dfs(idx,path):
            if idx == len(graph) - 1:
                ans.append(path[:])
                return
            
            if not graph[idx]:
                return 
            
            for node in graph[idx]:
                path.append(node)
                dfs(node,path)
                path.pop()       

        dfs(0,[0])
        return ans
        