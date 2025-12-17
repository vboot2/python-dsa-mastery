"""
Day 30: Trees, BST, Heaps

Binary Search Tree (BST) operations:
- Merge Two Binary Trees - recursion + combining node values
- Search in BST - recursive or iterative search
- Insert into BST - recursive insert at correct position
"""

# -------------------------------
# Example 1: Merge Two Binary Trees
# -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def merge_trees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    """
    Recursively merge t1 and t2.
    If both nodes exist, sum values.
    If one node is missing, take the other.
    """
    if not t1 and not t2:
        return None
    if not t1:
        return t2
    if not t2:
        return t1

    root = TreeNode(t1.val + t2.val)
    root.left = merge_trees(t1.left, t2.left)
    root.right = merge_trees(t1.right, t2.right)
    return root

print("Merge Trees Example: [1,3,2,5] + [2,1,3,None,4,None,7]")
t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
merged = merge_trees(t1, t2)
print("Merged Root Value:", merged.val)


# -------------------------------
# Example 2: Search in a Binary Search Tree
# -------------------------------
def search_bst(root: TreeNode, val: int) -> TreeNode:
    """
    Traverse left or right depending on BST property.
    """
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)

tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
found = search_bst(tree, 2)
print("Search Result:", found.val if found else None)


# -------------------------------
# Example 3: Insert into a Binary Search Tree
# -------------------------------
def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    """
    Recursively find correct spot and insert node.
    """
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

root = TreeNode(4, TreeNode(2), TreeNode(7))
root = insert_into_bst(root, 5)
print("Inserted node 5. Root Right Child:", root.right.val, "-> Left Child of Right:", root.right.left.val)
