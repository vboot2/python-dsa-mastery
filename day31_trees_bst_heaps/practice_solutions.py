"""
Day 31: Trees, BST, Heaps - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Validate Binary Search Tree (LeetCode 98, Medium)
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionValidateBST:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = [None]

        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if prev[0] is not None and node.val <= prev[0]:
                return False
            prev[0] = node.val
            return inorder(node.right)

        return inorder(root)


# ---------------------------------------------------------
# Problem 2: Kth Smallest Element in a BST (LeetCode 230, Medium)
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# ---------------------------------------------------------
class SolutionKthSmallest:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


# ---------------------------------------------------------
# Problem 3: Lowest Common Ancestor of a Binary Tree (LeetCode 236, Medium)
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# ---------------------------------------------------------
class SolutionLCA:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Validate BST
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    print("Valid BST:", SolutionValidateBST().isValidBST(tree))

    # Kth Smallest
    tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print("Kth Smallest (k=1):", SolutionKthSmallest().kthSmallest(tree, 1))

    # LCA
    p = TreeNode(5)
    q = TreeNode(1)
    root = TreeNode(3, p, q)
    lca = SolutionLCA().lowestCommonAncestor(root, p, q)
    print("LCA of 5 and 1:", lca.val)
