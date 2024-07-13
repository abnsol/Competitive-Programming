from collections import deque, defaultdict
import sys

input = sys.stdin.read

def is_bicolorable(n, edges):
    if n == 0:
        return False

    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    for node in range(1, n + 1):
        if color[node] == -1:
            if not bfs(node):
                return False
    
    return True



data = input().strip().split()

index = 0
results = []

while index < len(data):
    n = int(data[index])
    index += 1
    if n == 0:
        break
    
    l = int(data[index])
    index += 1
    edges = []
    
    for _ in range(l):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    if is_bicolorable(n, edges):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")


