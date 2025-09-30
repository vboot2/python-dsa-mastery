"""
Day 30: Trees, BST, Heaps - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Merge Two Binary Trees (LeetCode 617, Easy)
# Link: https://leetcode.com/problems/merge-two-binary-trees/
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionMergeTrees:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root


# ---------------------------------------------------------
# Problem 2: Search in a Binary Search Tree (LeetCode 700, Easy)
# Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
# ---------------------------------------------------------
class SolutionSearchBST:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)


# ---------------------------------------------------------
# Problem 3: Insert into a Binary Search Tree (LeetCode 701, Medium)
# Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# ---------------------------------------------------------
class SolutionInsertBST:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Merge Trees
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    merged = SolutionMergeTrees().mergeTrees(t1, t2)
    print("Merged Tree Root Value:", merged.val)

    # Search in BST
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    found = SolutionSearchBST().searchBST(tree, 2)
    print("Search in BST:", found.val if found else None)

    # Insert into BST
    root = TreeNode(4, TreeNode(2), TreeNode(7))
    root = SolutionInsertBST().insertIntoBST(root, 5)
    print("Inserted Node 5:", root.right.left.val)
