"""
Day 33: Trees, BST, Heaps

Binary Search Tree operations:
- In-order iteration with a BST Iterator
- Serializing and deserializing a tree
- Deleting a node in a BST
"""

from collections import deque

# -------------------------------
# Example 1: BST Iterator (In-order Traversal)
# -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# Example tree: [7,3,15,None,None,9,20]
root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
itr = BSTIterator(root)
print("BST Iterator traversal:", [itr.next() for _ in range(4)])


# -------------------------------
# Example 2: Serialize and Deserialize Binary Tree
# -------------------------------
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

codec = Codec()
serialized = codec.serialize(root)
print("Serialized tree:", serialized)
print("Deserialize + serialize again:", codec.serialize(codec.deserialize(serialized)))


# -------------------------------
# Example 3: Delete Node in a BST
# -------------------------------
def delete_node(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Find inorder successor
        succ = root.right
        while succ.left:
            succ = succ.left
        root.val = succ.val
        root.right = delete_node(root.right, succ.val)

    return root

# Delete 3 from BST [5,3,6,2,4,None,7]
sample = TreeNode(5)
sample.left = TreeNode(3, TreeNode(2), TreeNode(4))
sample.right = TreeNode(6, None, TreeNode(7))
new_root = delete_node(sample, 3)
print("Root after deleting 3:", new_root.val)
