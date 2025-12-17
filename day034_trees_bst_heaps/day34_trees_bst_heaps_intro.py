"""
Day 34: Trees, BST, Heaps

Constructing binary trees from traversals
and solving the **maximum path sum** problem.
"""

# -------------------------------
# Example 1: Construct from Preorder + Inorder
# -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTreePreIn(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    mid = inorder.index(root_val)
    root.left = buildTreePreIn(preorder[1:mid+1], inorder[:mid])
    root.right = buildTreePreIn(preorder[mid+1:], inorder[mid+1:])
    return root

pre = [3,9,20,15,7]
ino = [9,3,15,20,7]
root = buildTreePreIn(pre, ino)
print("Root from Pre+In:", root.val)


# -------------------------------
# Example 2: Construct from Inorder + Postorder
# -------------------------------
def buildTreeInPost(inorder, postorder):
    if not inorder or not postorder:
        return None

    root_val = postorder[-1]
    root = TreeNode(root_val)

    mid = inorder.index(root_val)
    root.left = buildTreeInPost(inorder[:mid], postorder[:mid])
    root.right = buildTreeInPost(inorder[mid+1:], postorder[mid:-1])
    return root

ino2 = [9,3,15,20,7]
post = [9,15,7,20,3]
root2 = buildTreeInPost(ino2, post)
print("Root from In+Post:", root2.val)


# -------------------------------
# Example 3: Binary Tree Maximum Path Sum
# -------------------------------
class SolutionMaxPath:
    def maxPathSum(self, root):
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)   # ignore negative paths
            right = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum

sample = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Max Path Sum:", SolutionMaxPath().maxPathSum(sample))
