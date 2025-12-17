"""
Day 37: Graphs, Union-Find, Tries - LeetCode Problem Solutions
"""

from collections import deque

# ---------------------------------------------------------
# Problem 1: Pacific Atlantic Water Flow (LeetCode 417, Medium)
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
# ---------------------------------------------------------
class SolutionPacificAtlantic:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols
                or (r, c) in visited or heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        return list(pac & atl)


# ---------------------------------------------------------
# Problem 2: Max Area of Island (LeetCode 695, Medium)
# Link: https://leetcode.com/problems/max-area-of-island/
# ---------------------------------------------------------
class SolutionMaxAreaOfIsland:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols
                or grid[r][c] == 0 or (r, c) in visited
            ):
                return 0
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        return max_area


# ---------------------------------------------------------
# Problem 3: Is Graph Bipartite (LeetCode 785, Medium)
# Link: https://leetcode.com/problems/is-graph-bipartite/
# ---------------------------------------------------------
class SolutionIsBipartite:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                queue = deque([node])
                color[node] = 0
                while queue:
                    curr = queue.popleft()
                    for nei in graph[curr]:
                        if nei not in color:
                            color[nei] = 1 - color[curr]
                            queue.append(nei)
                        elif color[nei] == color[curr]:
                            return False
        return True


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    print("Pacific Atlantic:", SolutionPacificAtlantic().pacificAtlantic(heights))

    grid = [
        [0,0,1,0,0],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [1,1,0,0,1]
    ]
    print("Max Area of Island:", SolutionMaxAreaOfIsland().maxAreaOfIsland(grid))

    print("Is Graph Bipartite:",
          SolutionIsBipartite().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
