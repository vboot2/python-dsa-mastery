"""
Day 145: Breadth-First Search (BFS)

BFS explores nodes level by level using a queue.
Common applications:
- Level order traversal of trees
- Shortest path in unweighted graphs
- Grid traversal (multi-source BFS)
"""

from collections import deque


# Example 1: Level Order Traversal of Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)

    return res


# Example 2: Shortest Path in Grid (Multi-source BFS)
def nearest_zero(mat):
    rows, cols = len(mat), len(mat[0])
    q = deque()
    dist = [[-1] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                q.append((r, c))
                dist[r][c] = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    return dist


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(level_order(root))

    mat = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]
    print(nearest_zero(mat))
