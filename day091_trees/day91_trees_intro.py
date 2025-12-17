""" Day 91: Trees  
More tree concepts — focusing on tree height/balance, tree correction, and structural flattening.
"""

# Example 1: Check if a tree is height-balanced
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def example_one():
    """
    Height-balanced definition:
    For every node,
    |height(left) - height(right)| <= 1
    """
    root = TreeNode(1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(5)
        )

    def check(node):
        if not node:
            return 0, True  # height, is_balanced

        lh, lb = check(node.left)
        rh, rb = check(node.right)

        balanced = lb and rb and abs(lh - rh) <= 1
        return max(lh, rh) + 1, balanced

    return check(root)[1]

print("Output Example 1:", example_one())


# Example 2: Flatten a tree (simple preorder list, conceptual demo)
def example_two():
    """
    Return preorder sequence as a list
    (Conceptual for flattening to array)
    """
    root = TreeNode(1, TreeNode(2), TreeNode(3))

    result = []

    def preorder(node):
        if not node:
            return
        result.append(node.val)
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return result

print("Output Example 2:", example_two())
