class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u,v = edges[0]
        for edge in edges:
            if u in edge and v in edge:
                continue
            elif u in edge:
                return u
            else:
                return v

            


