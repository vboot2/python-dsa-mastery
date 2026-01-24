"""Day 144: DFS - LeetCode Problem Solutions"""

from typing import List, Optional
from collections import defaultdict, deque


# ---------------------------------------------------------
# Problem: Populating Next Right Pointers in Each Node (LeetCode 116)
# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# ---------------------------------------------------------
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Optional[Node]" = None,
        right: "Optional[Node]" = None,
        next: "Optional[Node]" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class SolutionProblemOne:
    def connect(self, root):
        if not root:
            return None

        def dfs(node):
            if node.left:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return root


# ---------------------------------------------------------
# Problem: Populating Next Right Pointers in Each Node II (LeetCode 117)
# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def connect(self, root):
        if not root:
            return None

        cur = root
        while cur:
            dummy = tail = Node(0)
            while cur:
                for child in (cur.left, cur.right):
                    if child:
                        tail.next = child
                        tail = tail.next
                cur = cur.next
            cur = dummy.next
        return root


# ---------------------------------------------------------
# Problem: Lowest Common Ancestor of a BST (LeetCode 235)
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# ---------------------------------------------------------
class SolutionProblemThree:
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


# ---------------------------------------------------------
# Problem: Water and Jug Problem (LeetCode 365)
# Link: https://leetcode.com/problems/water-and-jug-problem/
# ---------------------------------------------------------
class SolutionProblemFour:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        from math import gcd

        return target <= jug1 + jug2 and target % gcd(jug1, jug2) == 0


# ---------------------------------------------------------
# Problem: Mini Parser (LeetCode 385)
# Link: https://leetcode.com/problems/mini-parser/
# ---------------------------------------------------------
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class SolutionProblemFive:
    def deserialize(self, s: str):
        if s[0] != "[":
            return NestedInteger(int(s))

        it = iter(s)

        def dfs():
            ni = NestedInteger()
            num = 0
            sign = 1
            has_num = False

            for c in it:
                if c == "-":
                    sign = -1

                elif c.isdigit():
                    num = num * 10 + int(c)
                    has_num = True

                elif c == "[":
                    ni.add(dfs())

                elif c == ",":
                    if has_num:
                        ni.add(NestedInteger(sign * num))
                        num = 0
                        sign = 1
                        has_num = False

                elif c == "]":
                    if has_num:
                        ni.add(NestedInteger(sign * num))
                    return ni

            return ni

        next(it)
        return dfs()


# ---------------------------------------------------------
# Problem: Lexicographical Numbers (LeetCode 386)
# Link: https://leetcode.com/problems/lexicographical-numbers/
# ---------------------------------------------------------
class SolutionProblemSix:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(curr):
            if curr > n:
                return
            res.append(curr)
            for i in range(10):
                dfs(curr * 10 + i)

        for i in range(1, 10):
            dfs(i)
        return res[:n]


# ---------------------------------------------------------
# Problem: Longest Absolute File Path (LeetCode 388)
# Link: https://leetcode.com/problems/longest-absolute-file-path/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def lengthLongestPath(self, input: str) -> int:
        stack = [0]
        res = 0

        for line in input.split("\n"):
            depth = line.count("\t")
            length = len(line.replace("\t", ""))
            while len(stack) > depth + 1:
                stack.pop()
            curr = stack[-1] + length
            stack.append(curr + 1)
            if "." in line:
                res = max(res, curr)
        return res


# ---------------------------------------------------------
# Problem: Flatten a Multilevel Doubly Linked List (LeetCode 430)
# Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# ---------------------------------------------------------
class Node:
    def __init__(
        self,
        val: int,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None,
        child: Optional["Node"] = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class SolutionProblemEight:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        def dfs(node: Node) -> Node:
            cur = node
            last = node

            while cur:
                nxt = cur.next
                if cur.child:
                    child_tail = dfs(cur.child)

                    cur.next = cur.child
                    cur.child.prev = cur
                    cur.child = None

                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    last = child_tail
                else:
                    last = cur

                cur = nxt

            return last

        if head:
            dfs(head)
        return head


# ---------------------------------------------------------
# Problem: Serialize and Deserialize BST (LeetCode 449)
# Link: https://leetcode.com/problems/serialize-and-deserialize-bst/
# ---------------------------------------------------------
class TreeNode:
    def __init__(
        self,
        x: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val: int = x
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class SolutionProblemNine:
    def serialize(self, root) -> str:
        res = []

        def dfs(node):
            if not node:
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return " ".join(res)

    def deserialize(self, data: str):
        if not data:
            return None

        vals = deque(map(int, data.split()))

        def dfs(lo, hi):
            if not vals or not (lo < vals[0] < hi):
                return None
            v = vals.popleft()
            node = TreeNode(v)
            node.left = dfs(lo, v)
            node.right = dfs(v, hi)
            return node

        return dfs(float("-inf"), float("inf"))


# ---------------------------------------------------------
# Problem: Concatenated Words (LeetCode 472)
# Link: https://leetcode.com/problems/concatenated-words/
# ---------------------------------------------------------
class SolutionProblemTen:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordSet and (suffix in wordSet or dfs(suffix)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False

        res = []
        for w in words:
            if dfs(w):
                res.append(w)
        return res


# ---------------------------------------------------------
# Problem: Freedom Trail (LeetCode 514)
# Link: https://leetcode.com/problems/freedom-trail/
# ---------------------------------------------------------
class SolutionProblemEleven:
    def findRotateSteps(self, ring: str, key: str):
        from functools import lru_cache

        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)

        @lru_cache(None)
        def dfs(i, k):
            if k == len(key):
                return 0
            res = float("inf")
            for j in pos[key[k]]:
                diff = abs(i - j)
                step = min(diff, len(ring) - diff)
                res = min(res, step + 1 + dfs(j, k + 1))
            return res

        return dfs(0, 0)


# ---------------------------------------------------------
# Problem: Contain Virus (LeetCode 749)
# Link: https://leetcode.com/problems/contain-virus/
# ---------------------------------------------------------
class SolutionProblemTwelve:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        while True:
            visited = [[0] * n for _ in range(m)]
            regions = []

            def dfs(i, j):
                stack = [(i, j)]
                region = [(i, j)]
                threat = set()
                walls = 0
                visited[i][j] = 1

                while stack:
                    x, y = stack.pop()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            if isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                stack.append((nx, ny))
                                region.append((nx, ny))
                            elif isInfected[nx][ny] == 0:
                                threat.add((nx, ny))
                                walls += 1

                return region, threat, walls

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        regions.append(dfs(i, j))

            if not regions:
                break

            idx = max(range(len(regions)), key=lambda i: len(regions[i][1]))
            res += regions[idx][2]

            for i, (region, _, _) in enumerate(regions):
                if i == idx:
                    for x, y in region:
                        isInfected[x][y] = -1
                else:
                    for x, y in region:
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and isInfected[nx][ny] == 0:
                                isInfected[nx][ny] = 1

        return res
