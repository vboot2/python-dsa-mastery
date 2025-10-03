"""
Day 33: Trees, BST, Heaps - LeetCode Problem Solutions
"""

from collections import deque

# ---------------------------------------------------------
# Problem 1: Binary Search Tree Iterator (LeetCode 173, Medium)
# Link: https://leetcode.com/problems/binary-search-tree-iterator/
# ---------------------------------------------------------
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        if node.right:
            self._leftmost_inorder(node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# ---------------------------------------------------------
# Problem 2: Serialize and Deserialize Binary Tree (LeetCode 297, Hard)
# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# ---------------------------------------------------------
class Codec:
    def serialize(self, root):
        if not root:
            return "N"

        q, res = deque([root]), []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")
        return ",".join(res)

    def deserialize(self, data):
        values = data.split(",")
        if values[0] == "N":
            return None

        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1
        return root


# ---------------------------------------------------------
# Problem 3: Delete Node in a BST (LeetCode 450, Medium)
# Link: https://leetcode.com/problems/delete-node-in-a-bst/
# ---------------------------------------------------------
class SolutionDeleteNode:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            succ = root.right
            while succ.left:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)

        return root


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # BST Iterator
    root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
    itr = BSTIterator(root)
    print("BST Iterator traversal:", [itr.next() for _ in range(4)])

    # Codec
    codec = Codec()
    serialized = codec.serialize(root)
    print("Serialized tree:", serialized)
    print("Deserialize + serialize again:", codec.serialize(codec.deserialize(serialized)))

    # Delete Node in BST
    sample = TreeNode(5)
    sample.left = TreeNode(3, TreeNode(2), TreeNode(4))
    sample.right = TreeNode(6, None, TreeNode(7))
    new_root = SolutionDeleteNode().deleteNode(sample, 3)
    print("Root after deleting 3:", new_root.val)
