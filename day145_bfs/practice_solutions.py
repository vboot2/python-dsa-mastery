"""
Day 145 BFS - LeetCode Practice Solutions
"""

from collections import deque
from typing import List, Optional, Deque, Tuple


# ---------------------------------------------------------
# Problem: Minimum Depth of Binary Tree (LeetCode 111)
# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# ---------------------------------------------------------
class TreeNode111:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode111"] = None,
        right: Optional["TreeNode111"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution111:
    def minDepth(self, root: Optional[TreeNode111]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            node, depth = q.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        return 0


# ---------------------------------------------------------
# Problem: Sum of Left Leaves (LeetCode 404)
# Link: https://leetcode.com/problems/sum-of-left-leaves/
# ---------------------------------------------------------
class TreeNode404:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution404:
    def sumOfLeftLeaves(self, root: Optional[TreeNode404]) -> int:
        if not root:
            return 0
        q = deque([(root, False)])
        total = 0
        while q:
            node, is_left = q.popleft()
            if is_left and not node.left and not node.right:
                total += node.val
            if node.left:
                q.append((node.left, True))
            if node.right:
                q.append((node.right, False))
        return total


# ---------------------------------------------------------
# Problem: Minimum Absolute Difference in BST (LeetCode 530)
# Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# ---------------------------------------------------------
class TreeNode530:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution530:
    def getMinimumDifference(self, root: Optional[TreeNode530]):
        prev = None
        res = float("inf")
        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if node:
                vals.append(node.val)
                q.append(node.left)
                q.append(node.right)
        vals.sort()
        for i in range(1, len(vals)):
            res = min(res, vals[i] - vals[i - 1])
        return res


# ---------------------------------------------------------
# Problem: Maximum Depth of N-ary Tree (LeetCode 559)
# Link: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# ---------------------------------------------------------
class Node559:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node559"]] = None
    ):
        self.val = val
        self.children = children


class Solution559:
    def maxDepth(self, root: "Node559") -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        max_depth = 0

        while q:
            node, depth = q.popleft()
            if depth > max_depth:
                max_depth = depth

            if node.children:
                for child in node.children:
                    q.append((child, depth + 1))

        return max_depth


# ---------------------------------------------------------
# Problem: Minimum Distance Between BST Nodes (LeetCode 783)
# Link: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# ---------------------------------------------------------
class TreeNode783:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution783:
    def minDiffInBST(self, root: Optional[TreeNode783]) -> int:
        vals = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                vals.append(node.val)
                q.append(node.left)
                q.append(node.right)
        vals.sort()
        return min(vals[i] - vals[i - 1] for i in range(1, len(vals)))


# ---------------------------------------------------------
# Problem: Univalued Binary Tree (LeetCode 965)
# Link: https://leetcode.com/problems/univalued-binary-tree/
# ---------------------------------------------------------
class TreeNode965:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution965:
    def isUnivalTree(self, root: Optional[TreeNode965]) -> bool:
        if root is None:
            return True

        val = root.val
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val != val:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True


# ---------------------------------------------------------
# Problem: Cousins in Binary Tree (LeetCode 993)
# Link: https://leetcode.com/problems/cousins-in-binary-tree/
# ---------------------------------------------------------
class TreeNode993:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution993:
    def isCousins(self, root: Optional[TreeNode993], x: int, y: int) -> bool:
        if not root:
            return False

        q: Deque[Tuple[TreeNode993, Optional[TreeNode993]]] = deque([(root, None)])

        while q:
            size = len(q)
            x_parent = y_parent = None

            for _ in range(size):
                node, parent = q.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            if x_parent or y_parent:
                return x_parent is not None and x_parent == y_parent is False

        return False


# ---------------------------------------------------------
# Problem: Find a Corresponding Node of a Binary Tree (LeetCode 1379)
# Link: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# ---------------------------------------------------------
class TreeNode1379:
    def __init__(
        self,
        x: int,
        left: Optional["TreeNode1379"] = None,
        right: Optional["TreeNode1379"] = None,
    ):
        self.val = x
        self.left = left
        self.right = right


class Solution1379:
    def getTargetCopy(
        self,
        original: Optional[TreeNode1379],
        cloned: Optional[TreeNode1379],
        target: Optional[TreeNode1379],
    ) -> Optional[TreeNode1379]:

        if original is None or cloned is None:
            return None

        q: deque[tuple[TreeNode1379, TreeNode1379]] = deque([(original, cloned)])

        while q:
            o, c = q.popleft()

            if o == target:
                return c

            if o.left and c.left:
                q.append((o.left, c.left))
            if o.right and c.right:
                q.append((o.right, c.right))

        return None


# ---------------------------------------------------------
# Problem: Binary Tree Level Order Traversal II (LeetCode 107)
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# ---------------------------------------------------------
class TreeNode107:
    def __init__(
        self,
        x: int,
        left: Optional["TreeNode107"] = None,
        right: Optional["TreeNode107"] = None,
    ):
        self.val = x
        self.left = left
        self.right = right


class Solution107:
    def levelOrderBottom(self, root: Optional[TreeNode107]) -> List[List[int]]:
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
        return res[::-1]


# ---------------------------------------------------------
# Problem: Minimum Genetic Mutation (LeetCode 433)
# Link: https://leetcode.com/problems/minimum-genetic-mutation/
# ---------------------------------------------------------
class Solution443:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bk = set(bank)
        q = deque([(startGene, 0)])
        genes = ["A", "C", "G", "T"]
        while q:
            s, steps = q.popleft()
            if s == endGene:
                return steps
            for i in range(len(s)):
                for g in genes:
                    nxt = s[:i] + g + s[i + 1 :]
                    if nxt in bk:
                        bk.remove(nxt)
                        q.append((nxt, steps + 1))
        return -1


# ---------------------------------------------------------
# Problem: Find Bottom Left Tree Value (LeetCode 513)
# Link: https://leetcode.com/problems/find-bottom-left-tree-value/
# ---------------------------------------------------------
class TreeNode513:
    def __init__(
        self,
        x: int,
        left: Optional["TreeNode513"] = None,
        right: Optional["TreeNode513"] = None,
    ):
        self.val = x
        self.left = left
        self.right = right


class Solution513:
    def findBottomLeftValue(self, root: Optional[TreeNode513]):
        if root is None:
            raise ValueError("Tree must have at least one node")

        q: deque[TreeNode513] = deque([root])
        res = root.val

        while q:
            node = q.popleft()
            res = node.val

            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return res


# ---------------------------------------------------------
# Problem: Minesweeper (LeetCode 529)
# Link: https://leetcode.com/problems/minesweeper/
# ---------------------------------------------------------
class Solution529:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
            return board

        rows, cols = len(board), len(board[0])
        q = deque([(r, c)])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while q:
            x, y = q.popleft()
            mines = 0
            neighbors = []
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if board[nx][ny] == "M":
                        mines += 1
                    else:
                        neighbors.append((nx, ny))
            if mines:
                board[x][y] = str(mines)
            else:
                board[x][y] = "B"
                for nx, ny in neighbors:
                    if board[nx][ny] == "E":
                        board[nx][ny] = "#"
                        q.append((nx, ny))
        return board


# ---------------------------------------------------------
# Problem: 01 Matrix (LeetCode 542)
# Link: https://leetcode.com/problems/01-matrix/
# ---------------------------------------------------------
class Solution542:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        q = deque()
        dist = [[-1] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))

        for r, c in q:
            pass

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return dist
