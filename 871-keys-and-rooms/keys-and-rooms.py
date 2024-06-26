class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(src):
            if src in visited:
                return 

            visited.add(src)            
            if len(visited) == len(rooms):
                return True

            boolean = False
            for i in rooms[src]:
                boolean = boolean or dfs(i)
            
            return boolean

        return dfs(0)
