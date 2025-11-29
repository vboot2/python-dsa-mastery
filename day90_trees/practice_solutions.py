""" Day 90: Trees - LeetCode Problem Solutions """

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---------------------------------------------------------
# Problem: Delete Nodes and Return Forest (LeetCode 1110, Medium)
# Link: https://leetcode.com/problems/delete-nodes-and-return-forest/
# ---------------------------------------------------------

class SolutionProblemOne:
    def delNodes(self, root, to_delete: List[int]) -> List:
        """
        Postorder traversal: delete children first, then parent.
        If a node is deleted, its children become new roots.
        """
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node, is_root):
            if not node:
                return None

            deleted = node.val in to_delete_set

            # If node is root and not deleted, add to forest
            if is_root and not deleted:
                forest.append(node)

            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            # Return None if deleted to cut it off
            return None if deleted else node

        dfs(root, True)
        return forest


# ---------------------------------------------------------
# Problem: Verify Preorder Serialization of a Binary Tree (LeetCode 331, Medium)
# Link: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# ---------------------------------------------------------

class SolutionProblemTwo:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        Use slot counting:
        - Start with 1 slot for the root.
        - Each node takes 1 slot.
        - Non-null nodes add 2 slots.
        """
        slots = 1
        nodes = preorder.split(",")

        for node in nodes:
            slots -= 1  # every node consumes a slot
            if slots < 0:
                return False

            if node != "#":
                slots += 2  # non-null node creates 2 new slots

        return slots == 0


# ---------------------------------------------------------
# Problem: Maximum Sum BST in Binary Tree (LeetCode 1373, Hard)
# Link: https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
# ---------------------------------------------------------

class SolutionProblemThree:
    def maxSumBST(self, root) -> int:
        """
        For each subtree return:
        - is_bst
        - min_val
        - max_val
        - sum_of_subtree
        Track global max sum.
        """
        self.max_sum = 0

        def dfs(node):
            if not node:
                return True, float('inf'), float('-inf'), 0

            left_bst, left_min, left_max, left_sum = dfs(node.left)
            right_bst, right_min, right_max, right_sum = dfs(node.right)

            # Check BST validity: left < node < right
            if left_bst and right_bst and left_max < node.val < right_min:
                total = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum, total)
                return True, min(left_min, node.val), max(right_max, node.val), total

            # Not a BST
            return False, 0, 0, 0

        dfs(root)
        return self.max_sum


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example: Can't test without tree input")
    print("Problem Two Example:", SolutionProblemTwo().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    print("Problem Three Example: depends on tree input")
