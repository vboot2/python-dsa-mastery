""" Day 91: Trees - LeetCode Problem Solutions """

from typing import Optional


# ---------------------------------------------------------
# Problem: Balanced Binary Tree (LeetCode 110, Easy)
# Link: https://leetcode.com/problems/balanced-binary-tree/
# ---------------------------------------------------------

class SolutionProblemOne:
    def isBalanced(self, root) -> bool:
        """
        Return (height, balanced) for each subtree.
        A tree is balanced if:
            |left_height - right_height| <= 1
        """
        def dfs(node):
            if not node:
                return 0, True

            lh, lb = dfs(node.left)
            rh, rb = dfs(node.right)

            balanced = lb and rb and abs(lh - rh) <= 1
            return max(lh, rh) + 1, balanced

        return dfs(root)[1]


# ---------------------------------------------------------
# Problem: Recover Binary Search Tree (LeetCode 99, Medium)
# Link: https://leetcode.com/problems/recover-binary-search-tree/
# ---------------------------------------------------------

class SolutionProblemTwo:
    def recoverTree(self, root) -> None:
        """
        Use inorder traversal:
        For a BST, inorder should be sorted.
        Two nodes will be out of order. Fix by swapping values.
        """
        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # Detect broken ordering
            if self.prev and self.prev.val > node.val:
                if not self.first:          # first violation
                    self.first = self.prev
                self.second = node          # second violation

            self.prev = node
            inorder(node.right)

        inorder(root)

        # Swap the two incorrect values
        self.first.val, self.second.val = self.second.val, self.first.val


# ---------------------------------------------------------
# Problem: Flatten Binary Tree to Linked List (LeetCode 114, Medium)
# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# ---------------------------------------------------------

class SolutionProblemThree:
    def flatten(self, root) -> None:
        """
        Flatten into linked list using reverse postorder:
        Traverse right -> left -> root
        Maintain a 'prev' pointer and link nodes accordingly.
        """
        self.prev = None

        def dfs(node):
            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node

        dfs(root)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example: Cannot test without full tree input")
    print("Problem Two Example: Inorder fix logic depends on tree input")
    print("Problem Three Example: Flatten modifies tree in-place")
