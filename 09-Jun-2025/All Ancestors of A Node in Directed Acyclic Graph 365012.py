# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize adjacency list for the graph
        adjacency_list = [[] for _ in range(n)]

        # Populate the adjacency list with reversed edges
        for edge in edges:
            from_node, to_node = edge
            adjacency_list[to_node].append(from_node)

        ancestors_list = []

        # For each node, find all its ancestors (children in reversed graph)
        for i in range(n):
            ancestors = []
            visited = set()
            self.find_children(i, adjacency_list, visited)
            # Add visited nodes to the current nodes' ancestor list
            for node in range(n):
                if node == i:
                    continue
                if node in visited:
                    ancestors.append(node)
            ancestors_list.append(ancestors)

        return ancestors_list

    # Helper method to perform DFS and find all children of a given node
    def find_children(self, current_node, adjacency_list, visited_nodes):
        # Mark current node as visited
        visited_nodes.add(current_node)

        # Recursively traverse all neighbors
        for neighbour in adjacency_list[current_node]:
            if neighbour not in visited_nodes:
                self.find_children(neighbour, adjacency_list, visited_nodes)