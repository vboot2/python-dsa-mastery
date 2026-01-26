"""
Day 146: BFS - LeetCode Problem Solutions
"""

from collections import deque
from typing import List, Optional, Set, Deque


# ---------------------------------------------------------
# Problem: Add One Row to Tree (LeetCode 623, Medium)
# Link: https://leetcode.com/problems/add-one-row-to-tree/
# ---------------------------------------------------------
class TreeNode623:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution623:
    def addOneRow(
        self, root: Optional[TreeNode623], val: int, depth: int
    ) -> Optional[TreeNode623]:
        if depth == 1:
            return TreeNode623(val, root, None)

        q = deque([root])
        level = 1

        while q:
            size = len(q)
            if level == depth - 1:
                for _ in range(size):
                    node = q.popleft()
                    node.left = TreeNode623(val, node.left, None)  # type: ignore
                    node.right = TreeNode623(  # type: ignore
                        val, None, node.right  # type: ignore
                    )  # pyright: ignore[reportOptionalMemberAccess]
                break

            for _ in range(size):
                node = q.popleft()
                if node.left:  # type: ignore
                    q.append(node.left)  # type: ignore
                if node.right:  # pyright: ignore[reportOptionalMemberAccess]
                    q.append(node.right)  # pyright: ignore[reportOptionalMemberAccess]
            level += 1

        return root


# ---------------------------------------------------------
# Problem: Print Binary Tree (LeetCode 655, Medium)
# Link: https://leetcode.com/problems/print-binary-tree/
# ---------------------------------------------------------
class TreeNode655:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode655"] = None,
        right: Optional["TreeNode655"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution655:
    def printTree(self, root: Optional[TreeNode655]) -> List[List[str]]:
        def height(node: Optional[TreeNode655]) -> int:
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return []

        h = height(root)
        rows, cols = h, (1 << h) - 1
        res = [["" for _ in range(cols)] for _ in range(rows)]

        q = deque([(root, 0, (cols - 1) // 2)])

        while q:
            node, r, c = q.popleft()
            res[r][c] = str(node.val)

            if r < h - 1:
                gap = 1 << (h - r - 2)

                if node.left:
                    q.append((node.left, r + 1, c - gap))
                if node.right:
                    q.append((node.right, r + 1, c + gap))

        return res


# ---------------------------------------------------------
# Problem: Maximum Width of Binary Tree (LeetCode 662, Medium)
# Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
# ---------------------------------------------------------
class TreeNode662:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode662"] = None,
        right: Optional["TreeNode662"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution662:
    def widthOfBinaryTree(self, root: Optional[TreeNode662]) -> int:
        if not root:
            return 0

        q: deque[tuple[TreeNode662, int]] = deque([(root, 0)])
        max_width = 0

        while q:
            level_len = len(q)
            _, first_idx = q[0]

            last_idx = first_idx

            for _ in range(level_len):
                node, idx = q.popleft()
                norm_idx = idx - first_idx

                last_idx = idx

                if node.left:
                    q.append((node.left, 2 * norm_idx))
                if node.right:
                    q.append((node.right, 2 * norm_idx + 1))

            level_width = last_idx - first_idx + 1
            max_width = max(max_width, level_width)

        return max_width


# ---------------------------------------------------------
# Problem: Bulb Switcher II (LeetCode 672, Medium)
# Link: https://leetcode.com/problems/bulb-switcher-ii/
# ---------------------------------------------------------
class Solution672:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        return 4 if presses == 1 else 7 if presses == 2 else 8


# ---------------------------------------------------------
# Problem: Employee Importance (LeetCode 690, Medium)
# Link: https://leetcode.com/problems/employee-importance/
# ---------------------------------------------------------
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution690:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        mp = {e.id: e for e in employees}
        q = deque([id])
        total = 0

        while q:
            eid = q.popleft()
            total += mp[eid].importance
            for sub in mp[eid].subordinates:
                q.append(sub)

        return total


# ---------------------------------------------------------
# Problem: Open the Lock (LeetCode 752, Medium)
# Link: https://leetcode.com/problems/open-the-lock/
# ---------------------------------------------------------
class Solution752:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        q = deque([("0000", 0)])
        visited = {"0000"}

        while q:
            state, steps = q.popleft()
            if state == target:
                return steps

            for i in range(4):
                for d in (-1, 1):
                    nxt = list(state)
                    nxt[i] = str((int(nxt[i]) + d) % 10)
                    nxt = "".join(nxt)
                    if nxt not in dead and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

        return -1


# ---------------------------------------------------------
# Problem: All Paths From Source to Target (LeetCode 797, Medium)
# Link: https://leetcode.com/problems/all-paths-from-source-to-target/
# ---------------------------------------------------------
class Solution797:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque([[0]])
        res = []

        while q:
            path = q.popleft()
            node = path[-1]
            if node == len(graph) - 1:
                res.append(path)
                continue
            for nei in graph[node]:
                q.append(path + [nei])

        return res


# ---------------------------------------------------------
# Problem: Smallest Subtree with all the Deepest Nodes (LeetCode 865, Medium)
# Link: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# ---------------------------------------------------------
class TreeNode865:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode865"] = None,
        right: Optional["TreeNode865"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(
        self, root: Optional[TreeNode865]
    ) -> Optional[TreeNode865]:
        if not root:
            return None

        q: deque[TreeNode865] = deque([root])
        deepest_nodes: List[TreeNode865] = []

        while q:
            deepest_nodes = list(q)
            next_q: deque[TreeNode865] = deque()
            for node in q:
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            q = next_q

        deepest_set: Set[TreeNode865] = set(deepest_nodes)

        def dfs(node: Optional[TreeNode865]) -> Optional[TreeNode865]:
            if not node:
                return None
            if node in deepest_set:
                return node

            left_res = dfs(node.left)
            right_res = dfs(node.right)

            if left_res and right_res:
                return node
            return left_res or right_res

        return dfs(root)


# ---------------------------------------------------------
# Problem: Snakes and Ladders (LeetCode 909, Medium)
# Link: https://leetcode.com/problems/snakes-and-ladders/
# ---------------------------------------------------------
class Solution909:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get(num):
            r = (num - 1) // n
            c = (num - 1) % n
            if r % 2:
                c = n - 1 - c
            return board[n - 1 - r][c]

        q = deque([(1, 0)])
        visited = {1}

        while q:
            pos, moves = q.popleft()
            if pos == n * n:
                return moves
            for nxt in range(pos + 1, min(pos + 6, n * n) + 1):
                val = get(nxt)
                dest = nxt if val == -1 else val
                if dest not in visited:
                    visited.add(dest)
                    q.append((dest, moves + 1))

        return -1


# ---------------------------------------------------------
# Problem: Complete Binary Tree Inserter (LeetCode 919, Medium)
# Link: https://leetcode.com/problems/complete-binary-tree-inserter/
# ---------------------------------------------------------
class TreeNode919:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode919"] = None,
        right: Optional["TreeNode919"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: Optional[TreeNode919]) -> None:
        self.root: Optional[TreeNode919] = root
        self._candidates: Deque[TreeNode919] = deque()

        if not root:
            return

        bfs: Deque[TreeNode919] = deque([root])
        while bfs:
            node = bfs.popleft()

            if not node.left or not node.right:
                self._candidates.append(node)

            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)

    def insert(self, val: int) -> int:
        parent = self._candidates[0]
        new_node = TreeNode919(val)

        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self._candidates.popleft()

        self._candidates.append(new_node)
        return parent.val

    def get_root(self) -> Optional[TreeNode919]:
        return self.root


# ---------------------------------------------------------
# Problem: Shortest Bridge (LeetCode 934, Medium)
# Link: https://leetcode.com/problems/shortest-bridge/
# ---------------------------------------------------------
class Solution934:
    def shortestBridge(self, grid: List[List[int]]):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        found = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break

        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            return steps
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            steps += 1


# ---------------------------------------------------------
# Problem: Check Completeness of a Binary Tree (LeetCode 958, Medium)
# Link: https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# ---------------------------------------------------------
class TreeNode958:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution958:
    def isCompleteTree(self, root: Optional[TreeNode958]) -> bool:
        q = deque([root])
        seen_null = False

        while q:
            node = q.popleft()
            if not node:
                seen_null = True
            else:
                if seen_null:
                    return False
                q.append(node.left)
                q.append(node.right)

        return True


# ---------------------------------------------------------
# Problem: Regions Cut By Slashes (LeetCode 959, Medium)
# Link: https://leetcode.com/problems/regions-cut-by-slashes/
# ---------------------------------------------------------
class Solution959:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        expanded = [[0] * (3 * n) for _ in range(3 * n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    expanded[i * 3][j * 3 + 2] = 1
                    expanded[i * 3 + 1][j * 3 + 1] = 1
                    expanded[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == "\\":
                    expanded[i * 3][j * 3] = 1
                    expanded[i * 3 + 1][j * 3 + 1] = 1
                    expanded[i * 3 + 2][j * 3 + 2] = 1

        def bfs(r, c):
            q = deque([(r, c)])
            expanded[r][c] = 1
            while q:
                x, y = q.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 3 * n and 0 <= ny < 3 * n and expanded[nx][ny] == 0:
                        expanded[nx][ny] = 1
                        q.append((nx, ny))

        regions = 0
        for i in range(3 * n):
            for j in range(3 * n):
                if expanded[i][j] == 0:
                    bfs(i, j)
                    regions += 1

        return regions


# ---------------------------------------------------------
# Problem: Numbers With Same Consecutive Differences (LeetCode 967, Medium)
# Link: https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# ---------------------------------------------------------
class Solution967:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = deque(range(1, 10))

        for _ in range(n - 1):
            for _ in range(len(q)):
                num = q.popleft()
                last = num % 10
                for d in {last + k, last - k}:
                    if 0 <= d <= 9:
                        q.append(num * 10 + d)

        return list(q)


# ---------------------------------------------------------
# Problem: Rotting Oranges (LeetCode 994, Medium)
# Link: https://leetcode.com/problems/rotting-oranges/
# ---------------------------------------------------------
class Solution994:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1
