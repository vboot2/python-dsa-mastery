"""
Day 56: BFS + Level Order

BFS processes nodes level-by-level — useful for traversal, aggregation, and distance-based problems.
"""

from collections import deque


# Example 1: Level order traversal of a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def example_one(root):
    """
    Perform level order traversal (BFS).
    Returns values at each level.
    """
    if not root:
        return []

    res, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res


# Example 2: BFS in a generic graph
def example_two(graph, start):
    """
    BFS traversal in an adjacency list graph.
    Returns order of visited nodes.
    """
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for nei in graph.get(node, []):
                if nei not in visited:
                    queue.append(nei)
    return order


# Construct binary tree for example_one
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Output Example 1:", example_one(root))
print("Output Example 2:", example_two({1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, 1))
