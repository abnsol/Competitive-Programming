class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        if not root:
            return []

        to_delete_set = set(to_delete)
        forest = []

        nodes_queue = deque([root])

        while nodes_queue:
            current_node = nodes_queue.popleft()

            if current_node.left:
                nodes_queue.append(current_node.left)
                # Disconnect the left child if it needs to be deleted
                if current_node.left.val in to_delete_set:
                    current_node.left = None

            if current_node.right:
                nodes_queue.append(current_node.right)
                # Disconnect the right child if it needs to be deleted
                if current_node.right.val in to_delete_set:
                    current_node.right = None

            # If the current node needs to be deleted, add its non-null children to the forest
            if current_node.val in to_delete_set:
                if current_node.left:
                    forest.append(current_node.left)
                if current_node.right:
                    forest.append(current_node.right)

        # Ensure the root is added to the forest if it is not to be deleted
        if root.val not in to_delete_set:
            forest.append(root)

        return forest