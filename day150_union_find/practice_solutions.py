"""
Day 150: Union-Find - LeetCode Problem Solutions
"""

from typing import List
from collections import defaultdict, Counter


# ---------------------------------------------------------
# Problem: Most Stones Removed with Same Row or Column (LeetCode 947, Medium)
# Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# ---------------------------------------------------------
class Solution947:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[find(x)] = find(y)

        for x, y in stones:
            union(x, ~y)

        roots = set(find(x) for x, _ in stones)
        return len(stones) - len(roots)


# ---------------------------------------------------------
# Problem: Number of Enclaves (LeetCode 1020, Medium)
# Link: https://leetcode.com/problems/number-of-enclaves/
# ---------------------------------------------------------
class Solution1020:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = list(range(m * n + 1))
        ocean = m * n

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[find(x)] = find(y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    idx = i * n + j
                    if i in (0, m - 1) or j in (0, n - 1):
                        union(idx, ocean)
                    for dx, dy in [(1, 0), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                            union(idx, ni * n + nj)

        return sum(
            grid[i][j] == 1 and find(i * n + j) != find(ocean)
            for i in range(m)
            for j in range(n)
        )


# ---------------------------------------------------------
# Problem: Smallest String With Swaps (LeetCode 1061, Medium)
# Link: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# ---------------------------------------------------------
class Solution1061:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            parent[max(px, py)] = min(px, py)

        for a, b in zip(s1, s2):
            union(ord(a) - 97, ord(b) - 97)

        return "".join(chr(find(ord(c) - 97) + 97) for c in baseStr)


# ---------------------------------------------------------
# Problem: Number of Closed Islands (LeetCode 1254, Medium)
# Link: https://leetcode.com/problems/number-of-closed-islands/
# ---------------------------------------------------------
class Solution1254:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = list(range(m * n + 1))
        border = m * n

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[find(x)] = find(y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    idx = i * n + j
                    if i in (0, m - 1) or j in (0, n - 1):
                        union(idx, border)
                    for dx, dy in [(1, 0), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                            union(idx, ni * n + nj)

        roots = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    r = find(i * n + j)
                    if r != find(border):
                        roots.add(r)
        return len(roots)


# ---------------------------------------------------------
# Problem: Validate Binary Tree Nodes (LeetCode 1361, Medium)
# Link: https://leetcode.com/problems/validate-binary-tree-nodes/
# ---------------------------------------------------------
class Solution1361:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        parent = list(range(n))
        indeg = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    indeg[child] += 1
                    if indeg[child] > 1:
                        return False
                    if find(i) == find(child):
                        return False
                    parent[find(child)] = find(i)

        roots = sum(indeg[i] == 0 for i in range(n))
        return roots == 1


# ---------------------------------------------------------
# Problem: Check if There is a Valid Path in a Grid (LeetCode 1391, Medium)
# Link: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
# ---------------------------------------------------------
class Solution1391:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = list(range(m * n))

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(a, b):
            uf[find(a)] = find(b)

        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }

        for i in range(m):
            for j in range(n):
                for dx, dy in dirs[grid[i][j]]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        if (-dx, -dy) in dirs[grid[ni][nj]]:
                            union(i * n + j, ni * n + nj)

        return find(0) == find(m * n - 1)


# ---------------------------------------------------------
# Problem: Detect Cycles in 2D Grid (LeetCode 1559, Medium)
# Link: https://leetcode.com/problems/detect-cycles-in-2d-grid/
# ---------------------------------------------------------
class Solution1559:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = list(range(m * n))

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        for i in range(m):
            for j in range(n):
                for dx, dy in [(1, 0), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[i][j] == grid[ni][nj]:
                        a, b = find(i * n + j), find(ni * n + nj)
                        if a == b:
                            return True
                        uf[a] = b
        return False


# ---------------------------------------------------------
# Problem: Checking Existence of Edge Length Limited Paths (LeetCode 1631, Medium)
# Link: https://leetcode.com/problems/path-with-minimum-effort/
# ---------------------------------------------------------
class Solution1631:
    def minimumEffortPath(self, heights: List[List[int]]):
        m, n = len(heights), len(heights[0])
        edges = []

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if i + 1 < m:
                    edges.append((abs(heights[i][j] - heights[i + 1][j]), idx, idx + n))
                if j + 1 < n:
                    edges.append((abs(heights[i][j] - heights[i][j + 1]), idx, idx + 1))

        edges.sort()

        parent = list(range(m * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                return True
            return False

        for w, u, v in edges:
            union(u, v)
            if find(0) == find(m * n - 1):
                return w

        return 0


# ---------------------------------------------------------
# Problem: Minimize Hamming Distance After Swap Operations (LeetCode 1722, Hard)
# Link: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
# ---------------------------------------------------------
class SolutionProblemSix:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in allowedSwaps:
            parent[find(a)] = find(b)

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        res = 0
        for idxs in groups.values():
            c1 = Counter(source[i] for i in idxs)
            c2 = Counter(target[i] for i in idxs)
            res += sum((c1 - c2).values())

        return res


# ---------------------------------------------------------
# Problem: Count Sub Islands (LeetCode 1905, Medium)
# Link: https://leetcode.com/problems/count-sub-islands/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            stack = [(i, j)]
            valid = True
            visited[i][j] = True

            while stack:
                x, y = stack.pop()
                if grid1[x][y] == 0:
                    valid = False
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and not visited[nx][ny]
                        and grid2[nx][ny] == 1
                    ):
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            return valid

        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    if dfs(i, j):
                        res += 1
        return res


# ---------------------------------------------------------
# Problem: Number of Good Paths (LeetCode 2316, Medium)
# Link: https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
# ---------------------------------------------------------
class Solution2316:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pv] = pu
                size[pu] += size[pv]

        comp = defaultdict(int)
        for i in range(n):
            comp[find(i)] += 1

        res = 0
        remaining = n
        for c in comp.values():
            remaining -= c
            res += c * remaining

        return res


# ---------------------------------------------------------
# Problem: Min Score of a Path Between Two Cities (LeetCode 2492, Medium)
# Link: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# ---------------------------------------------------------
class Solution2492:
    def minScore(self, n: int, roads: List[List[int]]):
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v, _ in roads:
            parent[find(u)] = find(v)

        root = find(1)
        ans = float("inf")
        for u, v, w in roads:
            if find(u) == root:
                ans = min(ans, w)
        return ans
