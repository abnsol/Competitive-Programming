# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque([0])

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node in visited:
                    continue

                visited.add(node)
                for nodes in rooms[node]:
                    q.append(nodes)
            
        return len(visited) == len(rooms)
                