"""
Day 146: Breadth-First Search (BFS)
BFS explores nodes level by level using a queue, making it ideal for shortest paths,
minimum depth, and level-order tree/graph problems.
"""

from collections import deque


# Example 1: Level-order traversal of a binary tree
def example_one():
    """
    BFS using a queue:
    - Push root
    - Process nodes level by level
    """

    class TreeNode:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    q = deque([root])
    result = []

    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return result


print("Output Example 1:", example_one())


# Example 2: Shortest path in an unweighted graph
def example_two():
    """
    BFS guarantees shortest path in unweighted graphs.
    """
    graph = {1: [2, 3], 2: [4], 3: [], 4: []}

    q = deque([(1, 0)])
    visited = set([1])

    while q:
        node, dist = q.popleft()
        if node == 4:
            return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))

    return -1


print("Output Example 2:", example_two())
