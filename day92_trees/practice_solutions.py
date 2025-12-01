""" Day 92: Trees - LeetCode Problem Solutions """

from typing import List, Optional


# ---------------------------------------------------------
# Problem: Convert Sorted Array to Binary Search Tree (LeetCode 108, Easy)
# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# ---------------------------------------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionProblemOne:
    def sortedArrayToBST(self, nums: List[int]):
        """
        Build height-balanced BST:
        - Middle element becomes root.
        - Recursively build children.
        """
        if not nums:
            return None

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(nums) - 1)


# ---------------------------------------------------------
# Problem: Binary Tree Postorder Traversal (LeetCode 145, Easy)
# Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
# ---------------------------------------------------------

class SolutionProblemTwo:
    def postorderTraversal(self, root) -> List[int]:
        """
        Recursive postorder:
        left -> right -> root
        """
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result


# ---------------------------------------------------------
# Problem: Flatten Nested List Iterator (LeetCode 341, Medium)
# Link: https://leetcode.com/problems/flatten-nested-list-iterator/
# ---------------------------------------------------------

class NestedInteger:
    """
    This is a placeholder class for the LeetCode-provided API.
    Real implementation is hidden on LC platform.
    """
    def isInteger(self) -> bool:
        pass
    def getInteger(self) -> int:
        pass
    def getList(self):
        pass

class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        """
        We flatten immediately using DFS.
        Store the result in an array,
        and iterate through it with an index pointer.
        """
        self.flat = []

        def dfs(ni):
            if ni.isInteger():
                self.flat.append(ni.getInteger())
            else:
                for x in ni.getList():
                    dfs(x)

        for item in nestedList:
            dfs(item)

        self.index = 0

    def next(self) -> int:
        value = self.flat[self.index]
        self.index += 1
        return value

    def hasNext(self) -> bool:
        return self.index < len(self.flat)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example: BST construction depends on tree printing")
    print("Problem Two Example: Cannot test without actual tree input")
    print("Problem Three Example: Nested iterator requires platform API")
