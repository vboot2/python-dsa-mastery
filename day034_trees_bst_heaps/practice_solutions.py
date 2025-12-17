"""
Day 34: Trees, BST, Heaps - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Construct Binary Tree from Preorder and Inorder Traversal (LeetCode 105, Medium)
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# ---------------------------------------------------------
class SolutionBuildPreIn:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


# ---------------------------------------------------------
# Problem 2: Construct Binary Tree from Inorder and Postorder Traversal (LeetCode 106, Medium)
# Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# ---------------------------------------------------------
class SolutionBuildInPost:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        return root


# ---------------------------------------------------------
# Problem 3: Binary Tree Maximum Path Sum (LeetCode 124, Hard)
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# ---------------------------------------------------------
class SolutionMaxPathSum:
    def maxPathSum(self, root):
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Pre+In
    pre = [3,9,20,15,7]
    ino = [9,3,15,20,7]
    root = SolutionBuildPreIn().buildTree(pre, ino)
    print("Pre+In root:", root.val)

    # In+Post
    ino2 = [9,3,15,20,7]
    post = [9,15,7,20,3]
    root2 = SolutionBuildInPost().buildTree(ino2, post)
    print("In+Post root:", root2.val)

    # Max Path Sum
    sample = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Max Path Sum:", SolutionMaxPathSum().maxPathSum(sample))
