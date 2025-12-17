"""
Day 36: Graphs, Union-Find, Tries

Graphs
- Word Ladder - BFS for shortest path in an implicit graph
- Clone Graph - DFS/BFS for graph traversal and copying
- Number of Islands - DFS/BFS for connected components in a grid
"""

from collections import deque, defaultdict

# -------------------------------
# Example 1: Word Ladder (BFS)
# -------------------------------
def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord not in wordList:
        return 0
    wordList = set(wordList)
    queue = deque([(beginWord, 1)])
    
    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + ch + word[i+1:]
                if new_word in wordList:
                    wordList.remove(new_word)
                    queue.append((new_word, steps + 1))
    return 0

print("Word Ladder Length:", ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))


# -------------------------------
# Example 2: Clone Graph (DFS)
# -------------------------------
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def cloneGraph(node: Node) -> Node:
    if not node:
        return None
    
    old_to_new = {}
    
    def dfs(curr):
        if curr in old_to_new:
            return old_to_new[curr]
        copy = Node(curr.val)
        old_to_new[curr] = copy
        for nei in curr.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    
    return dfs(node)

# Example: Simple 2-node graph
node1 = Node(1)
node2 = Node(2)
node1.neighbors = [node2]
node2.neighbors = [node1]
cloned = cloneGraph(node1)
print("Clone Graph Node Value:", cloned.val)


# -------------------------------
# Example 3: Number of Islands (DFS)
# -------------------------------
def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols 
            or grid[r][c] == '0' or (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count

grid_example = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print("Number of Islands:", numIslands(grid_example))
